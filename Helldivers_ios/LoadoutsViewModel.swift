import Foundation
import Combine
import SwiftUI

@MainActor
final class LoadoutsViewModel: ObservableObject {
    @Published var loadouts: [SquadLoadout] = [] {
        didSet {
            saveToStorage()
        }
    }
    @Published var isLoading: Bool = false
    @Published var errorMessage: String?

    private let baseURL = URL(string: "https://helldiversbackend-production.up.railway.app")!
    private var generateURL: URL { baseURL.appendingPathComponent("loadouts") }

    // UserDefaults key
    private let storageKey = "savedSquadLoadouts"

    init() {
        // load any saved loadouts at startup
        loadFromStorage()
    }

    // Persistence

    private func saveToStorage() {
        do {
            let data = try JSONEncoder().encode(loadouts)
            UserDefaults.standard.set(data, forKey: storageKey)
        } catch {
            print("⚠️ Failed to save loadouts: \(error)")
        }
    }

    private func loadFromStorage() {
        guard let data = UserDefaults.standard.data(forKey: storageKey) else { return }
        do {
            let decoded = try JSONDecoder().decode([SquadLoadout].self, from: data)
            self.loadouts = decoded
        } catch {
            print("⚠️ Failed to load loadouts: \(error)")
        }
    }

    // Networking

    func loadInitial() async {
        if loadouts.isEmpty {
            await generateLoadout(players: 4, style: "default", warbonds: [])
        }
    }

    func generateLoadout(players: Int, style: String, warbonds: [String]) async {
        isLoading = true
        errorMessage = nil
        defer { isLoading = false }

        do {
            var request = URLRequest(url: generateURL)
            request.httpMethod = "POST"
            request.setValue("application/json", forHTTPHeaderField: "Content-Type")

            let body = LoadoutRequest(players: players, warbonds: warbonds, style: style)
            request.httpBody = try JSONEncoder().encode(body)

            let (data, response) = try await URLSession.shared.data(for: request)

            guard let http = response as? HTTPURLResponse else {
                errorMessage = "Unexpected response from server."
                return
            }

            guard http.statusCode == 200 else {
                let serverMessage = String(data: data, encoding: .utf8) ?? ""
                errorMessage = "Server error \(http.statusCode): \(serverMessage)"
                return
            }

            let decoder = JSONDecoder()
            decoder.keyDecodingStrategy = .convertFromSnakeCase

            let apiResponse = try decoder.decode(APILoadoutResponse.self, from: data)
            let uiLoadout = apiResponse.toSquadLoadout(style: style)

            loadouts.append(uiLoadout)      

        } catch {
            errorMessage = "Failed to generate loadout: \(error.localizedDescription)"
        }
    }

    func delete(_ loadout: SquadLoadout) {
        if let index = loadouts.firstIndex(where: { $0.id == loadout.id }) {
            loadouts.remove(at: index)   
        }
    }
}
