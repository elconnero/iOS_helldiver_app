//
//  LoadoutsView.swift
//  Helldivers_ios
//
//  Created by Alvaro Contreras on 11/19/25.

import SwiftUI

struct Loadout: Identifiable {
    let id = UUID()
    let name: String
    let playerCount: Int
    let type: String
}

struct LoadoutsView: View {
    @State private var loadouts: [Loadout] = [
        Loadout(name: "Loadout 6", playerCount: 4, type: "Crowd Control"),
        Loadout(name: "Loadout 5", playerCount: 4, type: "Crowd Control"),
        Loadout(name: "Loadout 4", playerCount: 4, type: "Crowd Control"),
        Loadout(name: "Loadout 3", playerCount: 4, type: "Crowd Control"),
        Loadout(name: "Loadout 2", playerCount: 4, type: "Crowd Control"),
        Loadout(name: "Loadout 1", playerCount: 4, type: "Crowd Control")
    ]

    var body: some View {
        ZStack(alignment: .top) {
            Color.black
                .ignoresSafeArea()

            ScrollView {
                VStack(alignment: .leading, spacing: 16) {

                    Text("Loadouts")
                        .font(.custom("ChakraPetch-Bold", size: 34))
                        .foregroundColor(.white)
                        .frame(maxWidth: .infinity, alignment: .center)
                        .padding(.top, 24)
                        .padding(.bottom, 4)

                    ForEach(loadouts) { loadout in
                        LoadoutRow(loadout: loadout) {
                            if let index = loadouts.firstIndex(where: { $0.id == loadout.id }) {
                                loadouts.remove(at: index)
                            }
                        }
                    }

                    Spacer(minLength: 24)
                }
                .padding(.horizontal, 16)
                .padding(.bottom, 40)
            }
            .background(Color.clear)
        }
    }
}

struct LoadoutRow: View {
    let loadout: Loadout
    let onDelete: () -> Void

    var body: some View {
        ZStack {
            RoundedRectangle(cornerRadius: 18)
                .fill(Color.white.opacity(0.08))

            VStack(alignment: .leading, spacing: 12) {
                HStack {
                    Text(loadout.name)
                        .foregroundColor(.white)
                        .font(.system(size: 18, weight: .semibold))

                    Spacer()

                    Button(action: onDelete) {
                        Image(systemName: "xmark")
                            .font(.system(size: 14, weight: .bold))
                            .foregroundColor(.white.opacity(0.7))
                    }
                }

                Text("\(loadout.playerCount) Players | Type: \(loadout.type)")
                    .foregroundColor(.white.opacity(0.7))
                    .font(.system(size: 14))

                HStack {
                    Button {
                        // Need to hook this up to view loadout screen
                    } label: {
                        Text("View")
                            .font(.system(size: 16, weight: .semibold))
                            .foregroundColor(.black)
                            .padding(.horizontal, 28)
                            .padding(.vertical, 10)
                            .background(Color.helldiverYellow)
                            .clipShape(Capsule())
                    }

                    Spacer()

                    // Placeholder squares where the icons will go later
                    HStack(spacing: 8) {
                        ForEach(0..<5) { _ in
                            RoundedRectangle(cornerRadius: 6)
                                .fill(Color.white.opacity(0.16))
                                .frame(width: 28, height: 28)
                        }
                    }
                }
            }
            .padding(16)
        }
        .frame(maxWidth: .infinity)
    }
}
