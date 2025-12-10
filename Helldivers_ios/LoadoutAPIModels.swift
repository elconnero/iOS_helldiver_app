//
//  LoadoutAPIModels.swift
//  Helldivers_ios
//

import Foundation

// MARK: - Request

struct LoadoutRequest: Codable {
    let players: Int        // 1–4
    let warbonds: [String]  // e.g. ["ODST", "STEELED_VETERANS"]
    let style: String       // "default", "spec_ops", "explosive"
}

// MARK: - Response top-level

struct APILoadoutResponse: Codable {
    let players: [APIPlayer]
}

// MARK: - Player + loadout

struct APIPlayer: Codable {
    let player: Int
    let loadout: APILoadout
}

struct APILoadout: Codable {
    let primary: APIEquipment
    let secondary: APIEquipment
    let throwable: APIEquipment
    let armorPassive: APIEquipment?
    let booster: APIEquipment
    let stratagems: [APIEquipment]
}

// MARK: - Equipment

struct APIEquipment: Codable {
    let id: String?
    let name: String?
    let imageUrl: String?
}

// MARK: - Mapping to UI models

extension APILoadoutResponse {
    func toSquadLoadout(style: String) -> SquadLoadout {
        let uiPlayers = players.map { $0.toPlayerLoadout() }

        // Normalize style
        let normalized = style.lowercased()

        let uiType: LoadoutType
        switch normalized {
        case "default", "normal":
            uiType = .crowdControl          // shown as Normal
        case "spec_ops", "recon":
            uiType = .recon
        case "explosive":
            uiType = .explosive
        default:
            uiType = .crowdControl          // safe fallback
        }

        let index = Int.random(in: 1...999)
        return SquadLoadout(
            name: "Loadout \(index)",
            playerCount: uiPlayers.count,
            type: uiType,
            players: uiPlayers
        )
    }
}

extension APIPlayer {
    func toPlayerLoadout() -> PlayerLoadout {
        func mapItem(_ equip: APIEquipment?, fallbackName: String) -> EquipmentItem {
            equip?.toEquipmentItem()
            ?? EquipmentItem(
                id: UUID().uuidString,
                name: fallbackName,
                imageURL: ""
            )
        }

        return PlayerLoadout(
            playerNumber: player,  // API already gives 1-based
            primary: loadout.primary.toEquipmentItem(),
            secondary: loadout.secondary.toEquipmentItem(),
            throwable: loadout.throwable.toEquipmentItem(),
            armorPassive: mapItem(loadout.armorPassive, fallbackName: "Armor Passive"),
            booster: loadout.booster.toEquipmentItem(),
            stratagems: loadout.stratagems.map { $0.toEquipmentItem() }
        )
    }
}

extension APIEquipment {
    func toEquipmentItem() -> EquipmentItem {
        EquipmentItem(
            id: id ?? UUID().uuidString,
            name: name ?? "Unknown",
            imageURL: imageUrl ?? ""
        )
    }
}
