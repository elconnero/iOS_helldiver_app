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
            let mediumCardHeight = totalHeight * 0.14
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
                                      height: mediumCardHeight)
                        equipmentCard(item: player.throwable,
                                      height: mediumCardHeight)
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
                RoundedRectangle(cornerRadius: 16)
                    .fill(
                        LinearGradient(
                            colors: [
                                Color(red: 38.0/255.0, green: 38.0/255.0, blue: 38.0/255.0), // #262626
                                Color(red: 20.0/255.0, green: 20.0/255.0, blue: 20.0/255.0)  // #141414
                            ],
                            startPoint: .top,
                            endPoint: .bottom
                        )
                    )


                Text("") // dummy text to keep the closure syntactically happy if needed
                    .onAppear {
                        print("Image URL for \(item.name): \(item.imageURL)")
                    }
                AsyncImage(url: URL(string: item.imageURL)) { phase in
                    switch phase {
                    case .success(let image):
                        image
                            .resizable()
                            .scaledToFit()
                            .padding(large ? 0 : 8)

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
