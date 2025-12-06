//
//  LoadoutModels.swift
//  Helldivers_ios
//
//  Created by Alvaro Contreras on 11/29/25.
//

import Foundation

// Basic equipment item
struct EquipmentItem: Identifiable, Hashable, Codable {
    let id: String
    let name: String
    let imageURL: String
}

// Player loadout
struct PlayerLoadout: Identifiable, Hashable, Codable {
    var id: UUID = UUID()            // var + default value is fine
    let playerNumber: Int

    let primary: EquipmentItem
    let secondary: EquipmentItem
    let throwable: EquipmentItem
    let armorPassive: EquipmentItem
    let booster: EquipmentItem
    let stratagems: [EquipmentItem]
}

// Squad
enum LoadoutType: String, Codable {
    case crowdControl = "Crowd Control"
    case recon = "Recon"
    case explosive = "Explosive"
}

struct SquadLoadout: Identifiable, Hashable, Codable {
    var id: UUID = UUID()            // var + default value
    let name: String
    let playerCount: Int
    let type: LoadoutType
    let players: [PlayerLoadout]
}
