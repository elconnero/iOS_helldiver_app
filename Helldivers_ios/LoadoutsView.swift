import SwiftUI
import UIKit

struct LoadoutsView: View {
    @EnvironmentObject var viewModel: LoadoutsViewModel

    var body: some View {
        NavigationStack {
            ZStack(alignment: .top) {
                Color.black.ignoresSafeArea()

                ScrollView {
                    VStack(alignment: .leading, spacing: 24) {

                        // Title
                        Text("Loadouts")
                            .font(.custom("ChakraPetch-Bold", size: 34))
                            .foregroundColor(.white)
                            .frame(maxWidth: .infinity, alignment: .center)
                            .padding(.top, 24)

                        // Error message (if any)
                        if let error = viewModel.errorMessage {
                            Text(error)
                                .foregroundColor(.red)
                                .font(.system(size: 14))
                                .multilineTextAlignment(.center)
                                .padding(.horizontal, 8)
                        }

                        // Cards
                        ForEach(viewModel.loadouts) { loadout in
                            loadoutCard(loadout)
                        }
                    }
                    .padding(.horizontal, 16)
                    .padding(.bottom, 120)   // room for bottom tab bar
                }
            }
            .navigationBarBackButtonHidden(true)
            .task {
                await viewModel.loadInitial()
            }
        }
    }

    // Loadout Card

    @ViewBuilder
    private func loadoutCard(_ loadout: SquadLoadout) -> some View {
        let icons = summaryIcons(for: loadout)   // 4 stratagems + booster

        ZStack {
            RoundedRectangle(cornerRadius: 24)
                .fill(Color.white.opacity(0.06))

            VStack(alignment: .leading, spacing: 12) {

                // Top row: name + delete
                HStack {
                    Text(loadout.name)
                        .font(.system(size: 20, weight: .semibold))
                        .foregroundColor(.white)

                    Spacer()

                    Button {
                        viewModel.delete(loadout)
                    } label: {
                        Image(systemName: "xmark")
                            .foregroundColor(.white.opacity(0.7))
                            .font(.system(size: 16, weight: .bold))
                    }
                    .buttonStyle(.plain)
                }

                // Subtitle
                Text("\(loadout.playerCount) Players | Type: \(loadout.type.rawValue)")
                    .foregroundColor(.white.opacity(0.7))
                    .font(.system(size: 14))

                // Bottom row: View button + icon strip
                HStack {
                    NavigationLink {
                        SquadDetailView(squad: loadout)
                    } label: {
                        Text("View")
                            .font(.system(size: 16, weight: .semibold))
                            .foregroundColor(.black)
                            .frame(width: 96, height: 44)
                            .background(Color.helldiverYellow)
                            .cornerRadius(22)
                    }
                    .buttonStyle(.plain)

                    Spacer()

                    HStack(spacing: 8) {
                        // icons (up to 5: 4 stratagems + booster)
                        ForEach(icons, id: \.id) { item in
                            iconBox(for: item)
                        }

                        // Fill with empty slots so it always looks like 5
                        if icons.count < 5 {
                            ForEach(0..<(5 - icons.count), id: \.self) { _ in
                                RoundedRectangle(cornerRadius: 8)
                                    .fill(Color.white.opacity(0.10))
                                    .frame(width: 32, height: 32)
                            }
                        }
                    }
                }
                .padding(.top, 8)
            }
            .padding(16)
        }
        .frame(maxWidth: .infinity)
        .frame(height: 140)
    }

    // Icon Box

    @ViewBuilder
    private func iconBox(for item: EquipmentItem) -> some View {
        ZStack {
            // Grey slot background
            RoundedRectangle(cornerRadius: 8)
                .fill(Color.white.opacity(0.10))

            if !item.imageURL.isEmpty {
                RemoteImageView(urlString: item.imageURL)
                    .padding(4)
            }
        }
        .frame(width: 32, height: 32)
    }

    // Helpers

    // Returns 4 stratagems + booster from the first player
    private func summaryIcons(for squad: SquadLoadout) -> [EquipmentItem] {
        guard let first = squad.players.first else { return [] }

        #if DEBUG
        print("🔍 Summary for \(squad.name)")
        print("  Booster: \(first.booster.name) -> \(first.booster.imageURL)")
        for (i, s) in first.stratagems.enumerated() {
            print("  Strat \(i): \(s.name) -> \(s.imageURL)")
        }
        #endif

        let stratagems = Array(first.stratagems.prefix(4))
        return stratagems + [first.booster]
    }
}

//
// Remote Image Loader
//

final class RemoteImageLoader: ObservableObject {
    @Published var image: UIImage?

    private static let cache = NSCache<NSURL, UIImage>()
    private var url: URL?

    init(url: URL?) {
        self.url = url
        load()
    }

    private func load() {
        guard let url else { return }

        // Check cache first
        if let cached = Self.cache.object(forKey: url as NSURL) {
            self.image = cached
            return
        }

        URLSession.shared.dataTask(with: url) { data, response, error in
            guard
                let data,
                let uiImage = UIImage(data: data)
            else { return }

            Self.cache.setObject(uiImage, forKey: url as NSURL)

            DispatchQueue.main.async {
                self.image = uiImage
            }
        }.resume()
    }
}

struct RemoteImageView: View {
    @StateObject private var loader: RemoteImageLoader

    init(urlString: String) {
        let url = URL(string: urlString)
        _loader = StateObject(wrappedValue: RemoteImageLoader(url: url))
    }

    var body: some View {
        Group {
            if let uiImage = loader.image {
                Image(uiImage: uiImage)
                    .resizable()
                    .scaledToFit()
            } else {
                EmptyView()
            }
        }
    }
}

