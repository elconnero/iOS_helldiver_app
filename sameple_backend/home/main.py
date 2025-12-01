import os
import random
import json
from typing import Dict, Any, List, Set, Tuple

from backend.database.rawdata import (
    primary,
    secondary,
    throwable,
    Armor_Passive,
    Booster,
    Stratagems,
)
from backend.universal.enums import War_Bond, Style
from backend.universal.functionss import (
    build_pick_order,
    convert_warbond_strings_to_enums,
)

# ---------------------------------------------------------
# Global debugging & image base URL
# ---------------------------------------------------------

DEBUG: bool = False  # flip to True for noisy logs
IMAGE_BASE_URL = os.getenv("IMAGE_BASE_URL", "helldiversbackend-production.up.railway.app")
#, "http://127.0.0.1:8000"


def build_asset_url(slot: str, asset_id: str) -> str:
    """
    slot: 'primary', 'secondary', 'throwable', 'armor_passive', 'booster', 'strat'
    asset_id: e.g. '010101'
    """
    return f"{IMAGE_BASE_URL}/static/{slot}/{asset_id}.png"


# ---------------------------------------------------------
# Style helpers
# ---------------------------------------------------------


def convert_style_string_to_enum(style_str: str) -> Style:
    """
    Convert an incoming style string (e.g. 'default', 'spec_ops', 'explosive')
    into a Style enum. Falls back to Style.DEFAULT if it can't match.
    """
    style_str = style_str.lower().strip()

    for s in Style:
        if s.value.lower() == style_str:
            return s

    # fallback
    return Style.DEFAULT


def normalize_style_list(raw_styles: Any) -> List[Style]:
    """
    Normalize various possible representations of style info into
    List[Style].

    Accepts:
    - Style.DEFAULT
    - [Style.DEFAULT, Style.SPECOPS]
    - ["default", "spec_ops"]
    - []
    """
    if raw_styles is None:
        return []

    # Single Style enum
    if isinstance(raw_styles, Style):
        return [raw_styles]

    # List/tuple of things
    if isinstance(raw_styles, (list, tuple)):
        out: List[Style] = []
        for item in raw_styles:
            if isinstance(item, Style):
                out.append(item)
            elif isinstance(item, str):
                out.append(convert_style_string_to_enum(item))
        return out

    # Fallback
    if isinstance(raw_styles, str):
        return [convert_style_string_to_enum(raw_styles)]

    return []


def choose_by_style(candidates: List[Tuple], requested_style: Style) -> Tuple:
    """
    candidates: a list of tuples whose *last* element is List[Style].

    We weight candidates that contain requested_style more heavily, then
    pick via random.choices.
    """
    if not candidates:
        raise ValueError("choose_by_style called with no candidates")

    weights: List[int] = []
    for cand in candidates:
        styles: List[Style] = cand[-1]
        if requested_style in styles:
            weights.append(3)  # bias towards matching style
        else:
            weights.append(1)

    chosen = random.choices(candidates, weights=weights, k=1)[0]
    return chosen


# ---------------------------------------------------------
# Top-level entrypoint used by FastAPI
# ---------------------------------------------------------


def generate_loadouts_endpoint(request_body: Dict[str, Any]) -> Dict[str, Any]:
    """
    FastAPI handler (conceptually).

    request_body example:
    {
        "players": 4,
        "warbonds": ["BASE", "STEELED_VETERANS", "ODST"],  # user does NOT own these
        "style": "default"
    }
    """

    # 1. Extract input ---------------------------------------
    players: int = request_body["players"]
    warbonds_raw: List[str] = request_body["warbonds"]
    style_raw: str = request_body["style"]

    # 2. Convert warbond strings -> War_Bond enums (EXCLUDED warbonds)
    excluded_warbonds: Set[War_Bond] = convert_warbond_strings_to_enums(warbonds_raw)

    # 3. Convert style string to Style enum
    style_enum: Style = convert_style_string_to_enum(style_raw)

    if DEBUG:
        print(f"[DEBUG] players={players}")
        print(f"[DEBUG] excluded_warbonds={excluded_warbonds}")
        print(f"[DEBUG] style_enum={style_enum}")

    # 4. Generate all player loadouts ------------------------
    player_loadouts = generate_loadouts(
        players=players,
        excluded_warbonds=excluded_warbonds,
        style=style_enum,
    )

    # 5. Wrap in final JSON shape ---------------------------
    response: Dict[str, Any] = {
        "players": player_loadouts
    }

    return response


# ---------------------------------------------------------
# Orchestration for all players
# ---------------------------------------------------------


def generate_loadouts(
    players: int,
    excluded_warbonds: Set[War_Bond],
    style: Style,
) -> List[Dict[str, Any]]:
    """
    Orchestrates everything for all players.
    """

    # 1. Build pick order (who gets first dibs on subclasses)
    pick_order = build_pick_order(players)
    if DEBUG:
        print(f"[DEBUG] pick_order={pick_order}")

    # 2. Tracking sets so we avoid collisions
    used_primary_subclasses: Set[str] = set()   # e.g. {"Assault Rifle", "Shotgun"}
    used_asset_ids: Set[str] = set()            # covers *all* IDs across players

    player_loadouts: List[Dict[str, Any]] = []

    # 3. For each player in that order, build a full loadout
    for player in pick_order:
        loadout_record = generate_player_loadout(
            player=player,
            excluded_warbonds=excluded_warbonds,
            style=style,
            used_primary_subclasses=used_primary_subclasses,
            used_asset_ids=used_asset_ids,
        )
        player_loadouts.append(loadout_record)

    # 4. Sort back by player number if you want [1, 2, 3, 4] order:
    player_loadouts.sort(key=lambda rec: rec["player"])

    return player_loadouts


# ---------------------------------------------------------
# One player's loadout
# ---------------------------------------------------------


def generate_player_loadout(
    player: int,
    excluded_warbonds: Set[War_Bond],
    style: Style,
    used_primary_subclasses: Set[str],
    used_asset_ids: Set[str],
) -> Dict[str, Any]:
    """
    Build ONE player's loadout.
    """

    loadout: Dict[str, Any] = {}

    # 1. Primary -------------------------------------------------
    primary_id, primary_name, primary_subclass = pick_primary_for_player(
        excluded_warbonds=excluded_warbonds,
        style=style,
        used_primary_subclasses=used_primary_subclasses,
        used_asset_ids=used_asset_ids,
    )
    used_primary_subclasses.add(primary_subclass)
    used_asset_ids.add(primary_id)

    loadout["primary"] = {
        "id": primary_id,
        "name": primary_name,
        "image_url": build_asset_url("primary", primary_id),
    }

    # 2. Secondary ----------------------------------------------
    secondary_id, secondary_name = pick_secondary_for_player(
        excluded_warbonds=excluded_warbonds,
        style=style,
        used_asset_ids=used_asset_ids,
    )
    used_asset_ids.add(secondary_id)

    loadout["secondary"] = {
        "id": secondary_id,
        "name": secondary_name,
        "image_url": build_asset_url("secondary", secondary_id),
    }

    # 3. Throwable ----------------------------------------------
    throwable_id, throwable_name = pick_throwable_for_player(
        excluded_warbonds=excluded_warbonds,
        style=style,
        used_asset_ids=used_asset_ids,
    )
    used_asset_ids.add(throwable_id)

    loadout["throwable"] = {
        "id": throwable_id,
        "name": throwable_name,
        "image_url": build_asset_url("throwable", throwable_id),
    }

    # 4. Armor Passive ------------------------------------------
    armor_id, armor_name = pick_armor_passive_for_player(
        excluded_warbonds=excluded_warbonds,
        style=style,
        used_asset_ids=used_asset_ids,
    )
    used_asset_ids.add(armor_id)

    loadout["armor_passive"] = {
        "id": armor_id,
        "name": armor_name,
        "image_url": build_asset_url("armor_passive", armor_id),
    }

    # 5. Booster ------------------------------------------------
    booster_id, booster_name = pick_booster_for_player(
        excluded_warbonds=excluded_warbonds,
        style=style,
        used_asset_ids=used_asset_ids,
    )
    used_asset_ids.add(booster_id)

    loadout["booster"] = {
        "id": booster_id,
        "name": booster_name,
        "image_url": build_asset_url("booster", booster_id),
    }

    # 6. Stratagems ---------------------------------------------
    strat_list = pick_stratagems_for_player(
        excluded_warbonds=excluded_warbonds,
        style=style,
        used_asset_ids=used_asset_ids,
    )

    strat_objs = []
    for strat_id, strat_name in strat_list:
        used_asset_ids.add(strat_id)
        strat_objs.append(
            {
                "id": strat_id,
                "name": strat_name,
                "image_url": build_asset_url("strat", strat_id),
            }
        )

    loadout["stratagems"] = strat_objs

    # 7. Return record for API response -------------------------
    return {
        "player": player,
        "loadout": loadout,
    }


# ---------------------------------------------------------
# Primary picker
# ---------------------------------------------------------


def pick_primary_for_player(
    excluded_warbonds: Set[War_Bond],
    style: Style,
    used_primary_subclasses: Set[str],
    used_asset_ids: Set[str],
) -> Tuple[str, str, str]:
    """
    Choose a primary weapon ID, name, and its subclass for this player.
    Returns (weapon_id, weapon_name, subclass_name).

    - Enforces unique primary subclasses across players.
    - Enforces unique weapon IDs across players.
    - Respects excluded_warbonds.
    - Biases towards weapons whose Style tags contain requested style.
    """

    # 1. Get all primary subclasses from your data, excluding already-used ones
    available_subclasses: List[str] = [
        subclass_name
        for subclass_name in primary.keys()
        if subclass_name not in used_primary_subclasses
    ]

    if not available_subclasses:
        raise ValueError("No primary subclasses left to assign to a player.")

    random.shuffle(available_subclasses)

    if DEBUG:
        print(f"[DEBUG] Available PRIMARY subclasses: {available_subclasses}")

    # 2. Try each available subclass until we find valid candidates
    for subclass_name in available_subclasses:
        weapons_in_subclass = primary[subclass_name]  # list of (name, meta_dict)
        candidates: List[Tuple[str, str, List[Style]]] = []

        for weapon_name, meta in weapons_in_subclass:
            weapon_warbond: War_Bond = meta["Warbond"]
            weapon_id: str = meta["ID"]

            # Skip weapons from warbonds the user does NOT own
            if weapon_warbond in excluded_warbonds:
                if DEBUG:
                    print(
                        f"[DEBUG] [PRIMARY] Skip {weapon_name} ({weapon_id}) "
                        f"due to excluded warbond {weapon_warbond}"
                    )
                continue

            # Skip weapons already used by previous players
            if weapon_id in used_asset_ids:
                if DEBUG:
                    print(
                        f"[DEBUG] [PRIMARY] Skip {weapon_name} ({weapon_id}) already used"
                    )
                continue

            raw_styles = meta.get("Style", [])
            weapon_styles = normalize_style_list(raw_styles)

            candidates.append((weapon_id, weapon_name, weapon_styles))

        if candidates:
            chosen_id, chosen_name, chosen_styles = choose_by_style(
                candidates, style
            )
            if DEBUG:
                print(
                    f"[DEBUG] [PRIMARY] Style match {style}; "
                    f"chosen {chosen_name} ({chosen_id}) from subclass {subclass_name}"
                )
            return chosen_id, chosen_name, subclass_name

        if DEBUG:
            print(
                f"[DEBUG] No valid PRIMARY candidates in subclass '{subclass_name}'"
            )

    # If we exit the loop, no subclass had valid candidates
    raise ValueError("No valid primary weapons available after applying filters.")


# ---------------------------------------------------------
# Secondary picker
# ---------------------------------------------------------


def pick_secondary_for_player(
    excluded_warbonds: Set[War_Bond],
    style: Style,
    used_asset_ids: Set[str],
) -> Tuple[str, str]:
    """
    Choose a secondary weapon ID and its name for this player.
    Returns (weapon_id, weapon_name).

    - Secondary subclasses are allowed to repeat across players.
    - We only block reused weapon IDs (used_asset_ids).
    - Respects excluded_warbonds.
    - Biases towards weapons whose Style tags contain requested style.
    """

    available_subclasses: List[str] = list(secondary.keys())
    random.shuffle(available_subclasses)

    if DEBUG:
        print(f"[DEBUG] Available SECONDARY subclasses: {available_subclasses}")

    for subclass_name in available_subclasses:
        weapons_in_subclass = secondary[subclass_name]
        candidates: List[Tuple[str, str, List[Style]]] = []

        for weapon_name, meta in weapons_in_subclass:
            weapon_warbond: War_Bond = meta["Warbond"]
            weapon_id: str = meta["ID"]

            if weapon_warbond in excluded_warbonds:
                if DEBUG:
                    print(
                        f"[DEBUG] [SECONDARY] Skip {weapon_name} ({weapon_id}) "
                        f"due to excluded warbond {weapon_warbond}"
                    )
                continue

            if weapon_id in used_asset_ids:
                if DEBUG:
                    print(
                        f"[DEBUG] [SECONDARY] Skip {weapon_name} ({weapon_id}) already used"
                    )
                continue

            raw_styles = meta.get("Style", [])
            weapon_styles = normalize_style_list(raw_styles)

            candidates.append((weapon_id, weapon_name, weapon_styles))

        if candidates:
            chosen_id, chosen_name, chosen_styles = choose_by_style(
                candidates, style
            )
            if DEBUG:
                print(
                    f"[DEBUG] [SECONDARY] Style match {style}; "
                    f"chosen {chosen_name} ({chosen_id}) from subclass {subclass_name}"
                )
            return chosen_id, chosen_name

        if DEBUG:
            print(
                f"[DEBUG] No valid SECONDARY candidates in subclass '{subclass_name}'"
            )

    raise ValueError("No valid secondary weapons available after applying filters.")


# ---------------------------------------------------------
# Throwable picker
# ---------------------------------------------------------


def pick_throwable_for_player(
    excluded_warbonds: Set[War_Bond],
    style: Style,
    used_asset_ids: Set[str],
) -> Tuple[str, str]:
    """
    Choose a throwable ID and name for this player.
    Returns (throwable_id, throwable_name).

    - Throwable subclasses are allowed to repeat across players.
    - We only block reused IDs (used_asset_ids).
    - Respects excluded_warbonds.
    - Biases towards weapons whose Style tags contain requested style.
    """

    available_subclasses: List[str] = list(throwable.keys())
    random.shuffle(available_subclasses)

    if DEBUG:
        print(f"[DEBUG] Available THROWABLE subclasses: {available_subclasses}")

    for subclass_name in available_subclasses:
        throwables_in_subclass = throwable[subclass_name]
        candidates: List[Tuple[str, str, List[Style]]] = []

        for throwable_name, meta in throwables_in_subclass:
            throwable_warbond: War_Bond = meta["Warbond"]
            throwable_id: str = meta["ID"]

            if throwable_warbond in excluded_warbonds:
                if DEBUG:
                    print(
                        f"[DEBUG] [THROWABLE] Skip {throwable_name} ({throwable_id}) "
                        f"due to excluded warbond {throwable_warbond}"
                    )
                continue

            if throwable_id in used_asset_ids:
                if DEBUG:
                    print(
                        f"[DEBUG] [THROWABLE] Skip {throwable_name} ({throwable_id}) already used"
                    )
                continue

            raw_styles = meta.get("Style", [])
            throwable_styles = normalize_style_list(raw_styles)

            candidates.append((throwable_id, throwable_name, throwable_styles))

        if candidates:
            chosen_id, chosen_name, chosen_styles = choose_by_style(
                candidates, style
            )
            if DEBUG:
                print(
                    f"[DEBUG] [THROWABLE] Style match {style}; "
                    f"chosen {chosen_name} ({chosen_id}) from subclass {subclass_name}"
                )
            return chosen_id, chosen_name

        if DEBUG:
            print(
                f"[DEBUG] No valid THROWABLE candidates in subclass '{subclass_name}'"
            )

    raise ValueError("No valid throwable weapons available after applying filters.")


# ---------------------------------------------------------
# Armor Passive picker
# ---------------------------------------------------------


def pick_armor_passive_for_player(
    excluded_warbonds: Set[War_Bond],
    style: Style,
    used_asset_ids: Set[str],
) -> Tuple[str, str]:
    """
    Armor_Passive is a list of dicts: [{name: meta}, ...]
    meta["Warbond"] can be a War_Bond or a list of War_Bond.
    """

    candidates: List[Tuple[str, str, List[Style]]] = []

    for entry in Armor_Passive:
        # unpack the single key/value pair
        (armor_name, meta), = entry.items()

        warbond_field = meta["Warbond"]
        armor_id: str = meta["ID"]

        # Skip if this ID is already used
        if armor_id in used_asset_ids:
            if DEBUG:
                print(f"[DEBUG] [ARMOR] Skip {armor_name} ({armor_id}) already used")
            continue

        # Handle Warbond being either a single War_Bond or a list of War_Bond
        if isinstance(warbond_field, list):
            if any(wb in excluded_warbonds for wb in warbond_field):
                if DEBUG:
                    print(
                        f"[DEBUG] [ARMOR] Skip {armor_name} ({armor_id}) "
                        f"because one of {warbond_field} is excluded"
                    )
                continue
        else:
            if warbond_field in excluded_warbonds:
                if DEBUG:
                    print(
                        f"[DEBUG] [ARMOR] Skip {armor_name} ({armor_id}) "
                        f"due to excluded warbond {warbond_field}"
                    )
                continue

        raw_styles = meta.get("Tag", [])
        armor_styles = normalize_style_list(raw_styles)

        candidates.append((armor_id, armor_name, armor_styles))

    if not candidates:
        raise ValueError("No valid armor passive options after applying filters.")

    chosen_id, chosen_name, chosen_styles = choose_by_style(candidates, style)

    if DEBUG:
        print(f"[DEBUG] [ARMOR] chosen {chosen_name} ({chosen_id})")

    return chosen_id, chosen_name


# ---------------------------------------------------------
# Booster picker
# ---------------------------------------------------------


def pick_booster_for_player(
    excluded_warbonds: Set[War_Bond],
    style: Style,
    used_asset_ids: Set[str],
) -> Tuple[str, str]:
    """
    Booster is a list of dicts: [{name: meta}, ...]
    """
    candidates: List[Tuple[str, str, List[Style]]] = []

    for entry in Booster:
        (booster_name, meta), = entry.items()

        booster_wb = meta["Warbond"]
        booster_id: str = meta["ID"]

        if booster_id in used_asset_ids:
            if DEBUG:
                print(
                    f"[DEBUG] [BOOSTER] Skip {booster_name} ({booster_id}) already used"
                )
            continue

        if booster_wb in excluded_warbonds:
            if DEBUG:
                print(
                    f"[DEBUG] [BOOSTER] Skip {booster_name} ({booster_id}) "
                    f"due to excluded warbond {booster_wb}"
                )
            continue

        raw_styles = meta.get("Tag", [])
        booster_styles = normalize_style_list(raw_styles)

        candidates.append((booster_id, booster_name, booster_styles))

    if not candidates:
        raise ValueError("No valid booster options after applying filters.")

    chosen_id, chosen_name, chosen_styles = choose_by_style(candidates, style)

    if DEBUG:
        print(f"[DEBUG] [BOOSTER] chosen {chosen_name} ({chosen_id})")

    return chosen_id, chosen_name


# ---------------------------------------------------------
# Stratagem picker (Blue/Red/Green)
# ---------------------------------------------------------


def pick_stratagems_for_player(
    excluded_warbonds: Set[War_Bond],
    style: Style,
    used_asset_ids: Set[str],
) -> List[Tuple[str, str]]:
    """
    Pick 0–4 stratagems for this player, with rules:

    - 90% chance of exactly 4 stratagems.
    - 10% chance of between 0 and 3 (inclusive).
    - At most ONE 'pack' stratagem per player (Blue category uses 'pack' flag).
    - At most ONE 'Support' stratagem per player.
    - Avoid IDs already used by other players.
    - Respect excluded_warbonds.
    """

    # Decide how many stratagems this player gets
    if random.random() < 0.9:
        desired_count = 4
    else:
        desired_count = random.randint(0, 3)

    if desired_count == 0:
        if DEBUG:
            print("[DEBUG] [STRAT] Player rolled 0 stratagems")
        return []

    # Gather all candidates: (id, name, [styles], is_pack, is_support_slot)
    all_candidates: List[Tuple[str, str, List[Style], bool, bool]] = []

    for color_key, strat_map in Stratagems.items():
        # strat_map: { "MG-43 Machine Gun": { ... }, ... }
        for strat_name, meta in strat_map.items():
            strat_wb = meta["Warbond"]
            strat_id: str = meta["ID"]

            # Skip already-used IDs
            if strat_id in used_asset_ids:
                if DEBUG:
                    print(f"[DEBUG] [STRAT] Skip {strat_name} ({strat_id}) already used")
                continue

            # Respect excluded warbonds (can be single or list)
            if isinstance(strat_wb, list):
                if any(wb in excluded_warbonds for wb in strat_wb):
                    if DEBUG:
                        print(
                            f"[DEBUG] [STRAT] Skip {strat_name} ({strat_id}) "
                            f"because one of {strat_wb} is excluded"
                        )
                    continue
            else:
                if strat_wb in excluded_warbonds:
                    if DEBUG:
                        print(
                            f"[DEBUG] [STRAT] Skip {strat_name} ({strat_id}) "
                            f"due to excluded warbond {strat_wb}"
                        )
                    continue

            raw_styles = meta.get("Style", [])
            strat_styles = normalize_style_list(raw_styles)

            is_pack = bool(meta.get("pack", False))
            is_support_slot = bool(meta.get("Support", False))

            all_candidates.append(
                (strat_id, strat_name, strat_styles, is_pack, is_support_slot)
            )

    if not all_candidates:
        if DEBUG:
            print("[DEBUG] [STRAT] No candidates after filters")
        return []

    selected: List[Tuple[str, str]] = []
    pack_taken = False
    support_slot_filled = False

    # Work with a copy we can shrink
    pool = all_candidates[:]

    while len(selected) < desired_count and pool:
        weights: List[int] = []

        for (sid, sname, sstyles, is_pack, is_support_slot) in pool:
            # Block extra packs
            if pack_taken and is_pack:
                weights.append(0)
                continue

            # Block extra support-slot strats
            if support_slot_filled and is_support_slot:
                weights.append(0)
                continue

            # Normal style-based weighting
            if style in sstyles:
                weights.append(3)
            else:
                weights.append(1)

        if sum(weights) == 0:
            # Nothing valid left
            break

        idx = random.choices(range(len(pool)), weights=weights, k=1)[0]
        chosen_id, chosen_name, chosen_styles, is_pack, is_support_slot = pool.pop(idx)

        if is_pack:
            pack_taken = True

        if is_support_slot:
            support_slot_filled = True

        selected.append((chosen_id, chosen_name))

    if DEBUG:
        ids = [sid for sid, _ in selected]
        print(f"[DEBUG] [STRAT] selected IDs={ids}, desired={desired_count}")

    return selected


# ---------------------------------------------------------
# Local testing harness
# ---------------------------------------------------------


def main():
    # For local testing only – you can simulate a request_body here.
    fake_request = {
        "players": 4,
        # Warbonds the user does NOT own; these are excluded:
        "warbonds": ["STEELED_VETERANS", "ODST"],
        # Should match Style values: "default", "spec_ops", "explosive"
        "style": "spec_ops",
    }

    response = generate_loadouts_endpoint(fake_request)

    print("\n=== FINAL RESPONSE ===")
    print(json.dumps(response, indent=2))


if __name__ == "__main__":
    main()
