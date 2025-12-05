//
//  LoadoutModels.swift
//  Helldivers_ios
//
//  Created by Alvaro Contreras on 11/29/25.
//
//  UI-only mock models for now
//

import Foundation

// Basic equipment item
struct EquipmentItem: Identifiable, Hashable {
    let id: String
    let name: String
    let imageURL: String
}

// Player loadout
struct PlayerLoadout: Identifiable, Hashable {
    let id = UUID()
    let playerNumber: Int

    let primary: EquipmentItem
    let secondary: EquipmentItem
    let throwable: EquipmentItem
    let armorPassive: EquipmentItem
    let booster: EquipmentItem
    let stratagems: [EquipmentItem]
}

// Squad
enum LoadoutType: String {
    case crowdControl = "Crowd Control"
    case recon = "Recon"
    case explosive = "Explosive"
}

struct SquadLoadout: Identifiable, Hashable {
    let id = UUID()
    let name: String
    let playerCount: Int
    let type: LoadoutType
    let players: [PlayerLoadout]
}

enum MockLoadouts {
    static let sample: [SquadLoadout] = {

        // Equipment (same for all players)
        let primary = EquipmentItem(
            id: "010502",
            name: "SG-225 Breaker",
            imageURL: "https://helldiversbackend-production.up.railway.app/static/primary/010502.png"
        )

        let secondary = EquipmentItem(
            id: "020201",
            name: "CQC-19 Stun Lance",
            imageURL: "https://helldiversbackend-production.up.railway.app/static/secondary/020201.png"
        )

        let throwable = EquipmentItem(
            id: "030103",
            name: "G-10 Incendiary",
            imageURL: "https://helldiversbackend-production.up.railway.app/static/throwable/030103.png"
        )

        let armorPassive = EquipmentItem(
            id: "050102",
            name: "Advance Filtration",
            imageURL: "https://helldiversbackend-production.up.railway.app/static/armor_passive/050102.png"
        )

        let booster = EquipmentItem(
            id: "060101",
            name: "Hellpod Space Optimization",
            imageURL: "https://helldiversbackend-production.up.railway.app/static/booster/060101.png"
        )

        let strat1 = EquipmentItem(
            id: "040208",
            name: "Orbital Railcannon Strike",
            imageURL: "https://helldiversbackend-production.up.railway.app/static/strat/040208.png"
        )

        let strat2 = EquipmentItem(
            id: "040130",
            name: "MS-11 Solo Silo",
            imageURL: "https://helldiversbackend-production.up.railway.app/static/strat/040130.png"
        )

        let strat3 = EquipmentItem(
            id: "040103",
            name: "M-105 Stalwart",
            imageURL: "https://helldiversbackend-production.up.railway.app/static/strat/040103.png"
        )

        // Only 3 stratagems total ✅
        let stratagems = [strat1, strat2, strat3]

        // Create 4 players for UI testing
        let player1 = PlayerLoadout(
            playerNumber: 1,
            primary: primary,
            secondary: secondary,
            throwable: throwable,
            armorPassive: armorPassive,
            booster: booster,
            stratagems: stratagems
        )

        let player2 = PlayerLoadout(
            playerNumber: 2,
            primary: primary,
            secondary: secondary,
            throwable: throwable,
            armorPassive: armorPassive,
            booster: booster,
            stratagems: stratagems
        )

        let player3 = PlayerLoadout(
            playerNumber: 3,
            primary: primary,
            secondary: secondary,
            throwable: throwable,
            armorPassive: armorPassive,
            booster: booster,
            stratagems: stratagems
        )

        let player4 = PlayerLoadout(
            playerNumber: 4,
            primary: primary,
            secondary: secondary,
            throwable: throwable,
            armorPassive: armorPassive,
            booster: booster,
            stratagems: stratagems
        )

        let players = [player1, player2, player3, player4]

        // Build 6 different squad loadouts
        return (1...6).map { index in
            SquadLoadout(
                name: "Loadout \(index)",
                playerCount: players.count,
                type: .crowdControl,
                players: players
            )
        }
    }()
}
