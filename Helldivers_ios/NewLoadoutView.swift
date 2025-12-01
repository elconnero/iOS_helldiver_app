//
//  NewLoadoutView.swift
//  Helldivers_ios
//
//  Created by Alvaro Contreras on 11/19/25.

import SwiftUI

extension Color {
    static let helldiverYellow = Color(red: 1.0, green: 231/255.0, blue: 16/255.0)
}

struct NewLoadoutView: View {
    
    enum LoadoutType: String, CaseIterable {
        case normal = "Normal"
        case recon = "Recon"
        case explosive = "Explosive"
    }
    
    @State private var selectedPlayers: Int = 4
    @State private var selectedType: LoadoutType = .normal
    
    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()
            
            VStack(alignment: .leading, spacing: 32) {
                
                // Title
                Text("New Loadout")
                    .font(.custom("ChakraPetch-Bold", size: 34))
                    .foregroundColor(.white)
                    .frame(maxWidth: .infinity, alignment: .center)
                    .padding(.top, 24)
                
                // Player count
                VStack(alignment: .leading, spacing: 12) {
                    Text("How many players?")
                        .foregroundColor(.white)
                        .font(.system(size: 16, weight: .semibold))
                    
                    HStack(spacing: 12) {
                        ForEach(1...4, id: \.self) { num in
                            Button {
                                selectedPlayers = num
                            } label: {
                                Text("\(num)")
                                    .font(.system(size: 18, weight: .semibold))
                                    .frame(maxWidth: .infinity)
                                    .frame(height: 48)
                                    .background(
                                        RoundedRectangle(cornerRadius: 12)
                                            .fill(num == selectedPlayers
                                                  ? Color.helldiverYellow
                                                  : Color.white.opacity(0.12))
                                    )
                                    .foregroundColor(num == selectedPlayers ? .black : .white)
                            }
                            .buttonStyle(.plain)
                        }
                    }
                }
                
                // Loadout Type
                VStack(alignment: .leading, spacing: 12) {
                    Text("Loadout Type")
                        .foregroundColor(.white)
                        .font(.system(size: 16, weight: .semibold))
                    
                    HStack(spacing: 0) {
                        ForEach(LoadoutType.allCases, id: \.self) { type in
                            Button {
                                selectedType = type
                            } label: {
                                Text(type.rawValue)
                                    .font(.system(size: 16, weight: .semibold))
                                    .frame(maxWidth: .infinity)
                                    .frame(height: 44)
                                    .background(
                                        Group {
                                            if selectedType == type {
                                                Color.helldiverYellow
                                            } else {
                                                Color.clear
                                            }
                                        }
                                    )
                                    .foregroundColor(
                                        selectedType == type ? .black : .white
                                    )
                            }
                            .buttonStyle(.plain)
                        }
                    }
                    .padding(.horizontal, 4)
                    .background(Color.white.opacity(0.12))
                    .clipShape(Capsule())
                }
                
                Spacer()
                
                // Create Loadout
                Button {
                    // hook up to backend
                    print("Create Loadout tapped with \(selectedPlayers) players, type \(selectedType.rawValue)")
                } label: {
                    HStack(spacing: 8) {
                        Image(systemName: "star.fill")
                            .font(.system(size: 18, weight: .bold))
                        Text("Create Loadout")
                            .font(.system(size: 18, weight: .semibold))
                    }
                    .foregroundColor(.black)
                    .padding(.vertical, 14)
                    .frame(maxWidth: 340)
                    .background(Color.helldiverYellow)
                    .cornerRadius(24)
                }
                .frame(maxWidth: .infinity)
                .padding(.bottom, 40)
            }
            .padding(.horizontal, 24)
        }
    }
}

#Preview {
    NewLoadoutView()
}
