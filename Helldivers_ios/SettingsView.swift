//
//  SettingsView.swift
//  Helldivers_ios
//
//  Created by Alvaro Contreras on 11/19/25.

import SwiftUI

struct SettingsView: View {

    // Persistent storage for the names
    @AppStorage("player1Name") private var player1Name = "Player 1"
    @AppStorage("player2Name") private var player2Name = "Player 2"
    @AppStorage("player3Name") private var player3Name = "Player 3"
    @AppStorage("player4Name") private var player4Name = "Player 4"

    // Temp fields used for editing
    @State private var username1 = ""
    @State private var username2 = ""
    @State private var username3 = ""
    @State private var username4 = ""

    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()

            ScrollView {
                VStack(alignment: .leading, spacing: 24) {

                    Text("Settings")
                        .font(.custom("ChakraPetch-Bold", size: 34))
                        .foregroundColor(.white)
                        .frame(maxWidth: .infinity, alignment: .center)
                        .padding(.top, 20)

                    // Username fields
                    Group {
                        usernameField(label: "Username 1", text: $username1)
                        usernameField(label: "Username 2", text: $username2)
                        usernameField(label: "Username 3", text: $username3)
                        usernameField(label: "Username 4", text: $username4)
                    }

                    Spacer(minLength: 32)

                    // Save button
                    Button(action: saveUsernames) {
                        HStack(spacing: 8) {
                            Image(systemName: "square.and.arrow.down")
                                .font(.system(size: 18, weight: .bold))
                            Text("Save")
                                .font(.system(size: 18, weight: .semibold))
                        }
                        .foregroundColor(.black)
                        .frame(width: 140, height: 48)
                        .background(Color.helldiverYellow)
                        .cornerRadius(16)
                    }
                    .frame(maxWidth: .infinity, alignment: .center)
                    .padding(.bottom, 40)
                }
                .padding(.horizontal, 24)
            }
        }
        .onAppear {
            // Pre-fill text fields with existing saved names
            username1 = player1Name
            username2 = player2Name
            username3 = player3Name
            username4 = player4Name
        }
    }

    // Save Logic
    func saveUsernames() {
        if !username1.isEmpty { player1Name = username1 }
        if !username2.isEmpty { player2Name = username2 }
        if !username3.isEmpty { player3Name = username3 }
        if !username4.isEmpty { player4Name = username4 }

        print("Saved:", player1Name, player2Name, player3Name, player4Name)
    }

    // Field builder
    func usernameField(label: String, text: Binding<String>) -> some View {
        VStack(alignment: .leading, spacing: 6) {
            Text(label)
                .foregroundColor(.white)
                .font(.system(size: 16, weight: .semibold))

            ZStack(alignment: .leading) {
                RoundedRectangle(cornerRadius: 10)
                    .fill(Color.white.opacity(0.10))
                    .frame(height: 48)

                if text.wrappedValue.isEmpty {
                    Text("Enter Username")
                        .foregroundColor(Color.white.opacity(0.35))
                        .font(.system(size: 16))
                        .padding(.horizontal, 16)
                }

                TextField("", text: text)
                    .foregroundColor(.white)
                    .font(.system(size: 16))
                    .padding(.horizontal, 16)
            }
        }
    }
}
