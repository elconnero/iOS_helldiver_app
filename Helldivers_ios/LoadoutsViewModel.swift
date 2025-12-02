import Foundation
import Combine    // or `import SwiftUI`

@MainActor
final class LoadoutsViewModel: ObservableObject {
    @Published var loadouts: [SquadLoadout] = []
    @Published var isLoading: Bool = false
    @Published var errorMessage: String?

    private let baseURL = URL(string: "https://helldiversbackend-production.up.railway.app")!

    private var generateURL: URL {
        baseURL.appendingPathComponent("loadouts")
    }

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

            if let jsonString = String(data: data, encoding: .utf8) {
                print("Status code:", http.statusCode)
                print("Raw JSON response:", jsonString)
            } else {
                print("Status code:", http.statusCode)
                print("Raw JSON response: <non-UTF8 data>")
            }

            // 🚫 If it's not 200, don't try to decode as a loadout
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
            if let decodingError = error as? DecodingError {
                print("Decoding error:", decodingError)
            } else {
                print("Other error:", error)
            }
            errorMessage = "Failed to generate loadout: \(error.localizedDescription)"
        }
    }


    func delete(_ loadout: SquadLoadout) {
        if let index = loadouts.firstIndex(where: { $0.id == loadout.id }) {
            loadouts.remove(at: index)
        }
    }
}

