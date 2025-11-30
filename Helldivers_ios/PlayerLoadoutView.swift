//
//  PlayerLoadoutView.swift
//  Helldivers_ios
//
//  Created by Alvaro Contreras on 11/29/25.
//

import SwiftUI

struct PlayerLoadoutView: View {
    let player: PlayerLoadout
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        GeometryReader { geo in
            let totalHeight = geo.size.height
            let largeCardHeight = totalHeight * 0.22
            let smallCardHeight = totalHeight * 0.10
            let verticalSpacing: CGFloat = 12

            ZStack {
                Color.black.ignoresSafeArea()

                VStack(spacing: verticalSpacing) {

                    // Title
                    Text("Player \(player.playerNumber)")
                        .font(.custom("ChakraPetch-Bold", size: 34))
                        .foregroundColor(.white)
                        .frame(maxWidth: .infinity, alignment: .center)
                        .padding(.top, 12)

                    // Primary (big card)
                    equipmentCard(
                        item: player.primary,
                        large: true,
                        height: largeCardHeight
                    )

                    // Secondary + Throwable
                    HStack(spacing: 16) {
                        equipmentCard(item: player.secondary,
                                      height: smallCardHeight)
                        equipmentCard(item: player.throwable,
                                      height: smallCardHeight)
                    }

                    // Bottom grid
                    let bottomItems: [EquipmentItem] =
                        [player.armorPassive, player.booster] + player.stratagems

                    LazyVGrid(
                        columns: [
                            GridItem(.flexible(), spacing: 16),
                            GridItem(.flexible(), spacing: 16),
                            GridItem(.flexible(), spacing: 16)
                        ],
                        spacing: 16
                    ) {
                        ForEach(bottomItems) { item in
                            equipmentCard(item: item,
                                          height: smallCardHeight)
                        }
                    }

                    Spacer(minLength: 8)
                }
                .padding(.horizontal, 24)
                .padding(.bottom, 16)
            }
        }
    }

    // Card builder

    @ViewBuilder
    private func equipmentCard(
        item: EquipmentItem,
        large: Bool = false,
        height: CGFloat
    ) -> some View {
        VStack(spacing: 8) {
            ZStack {
                RoundedRectangle(cornerRadius: 18)
                    .fill(Color.white.opacity(0.06))

                AsyncImage(url: URL(string: item.imageURL)) { phase in
                    switch phase {
                    case .success(let image):
                        image
                            .resizable()
                            .scaledToFit()
                            .padding(large ? 24 : 16)

                    case .failure(_):
                        Image(systemName: "exclamationmark.triangle")
                            .resizable()
                            .scaledToFit()
                            .padding(large ? 32 : 20)
                            .foregroundColor(.white.opacity(0.7))

                    case .empty:
                        ProgressView()
                            .tint(.white)

                    @unknown default:
                        ProgressView()
                            .tint(.white)
                    }
                }
            }
            .frame(height: height)

            Text(item.name)
                .font(.system(size: 14, weight: .semibold))
                .foregroundColor(.white)
                .multilineTextAlignment(.center)
        }
    }
}
