//
//  LoadoutStore.swift
//  Helldivers_ios
//
//  Created by csuftitan on 12/5/25.
//

import Foundation
import Combine

final class LoadoutStore: ObservableObject {
    @Published var loadouts: [SquadLoadout] = []
    
    private let storageKey = "savedSquadLoadouts"
    
    init() {
        load()         
    }
    
    func save() {
        do {
            let data = try JSONEncoder().encode(loadouts)
            UserDefaults.standard.set(data, forKey: storageKey)
        } catch {
            print("⚠️ Failed to save loadouts: \(error)")
        }
    }
    
    private func load() {
        guard let data = UserDefaults.standard.data(forKey: storageKey) else { return }
        do {
            loadouts = try JSONDecoder().decode([SquadLoadout].self, from: data)
        } catch {
            print("⚠️ Failed to load loadouts: \(error)")
        }
    }
}
