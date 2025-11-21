//
//  SettingsView.swift
//  Helldivers_ios
//
//  Created by Alvaro Contreras on 11/19/25.

import SwiftUI

struct SettingsView: View {
    @State private var username1 = ""
    @State private var username2 = ""
    @State private var username3 = ""
    @State private var username4 = ""

    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()

            ScrollView {
                VStack(alignment: .leading, spacing: 24) {

                    // Title
                    Text("Settings")
                        .font(.custom("ChakraPetch-Bold", size: 34))
                        .foregroundColor(.white)
                        .frame(maxWidth: .infinity, alignment: .center)
                        .padding(.top, 20)

                    // MARK: - Username Fields
                    Group {
                        usernameField(label: "Username 1", text: $username1)
                        usernameField(label: "Username 2", text: $username2)
                        usernameField(label: "Username 3", text: $username3)
                        usernameField(label: "Username 4", text: $username4)
                    }

                    Spacer(minLength: 32)

                    // Save button
                    Button(action: {
                        print("Save tapped")
                        // add save logic
                    }) {
                        HStack(spacing: 8) {
                            Image(systemName: "square.and.arrow.down")
                                .font(.system(size: 18, weight: .bold))
                            Text("Save")
                                .font(.system(size: 18, weight: .semibold))
                        }
                        .foregroundColor(.black)
                        .frame(width: 140, height: 48)
                        .background(Color.yellow)
                        .cornerRadius(16)
                    }
                    .frame(maxWidth: .infinity, alignment: .center)
                    .padding(.bottom, 40)
                }
                .padding(.horizontal, 24)
            }
        }
    }

    // Fields here
    func usernameField(label: String, text: Binding<String>) -> some View {
        VStack(alignment: .leading, spacing: 6) {
            Text(label)
                .foregroundColor(.white)
                .font(.system(size: 16, weight: .semibold))

            ZStack(alignment: .leading) {
                // background rectangle
                RoundedRectangle(cornerRadius: 10)
                    .fill(Color.white.opacity(0.10))
                    .frame(height: 48)

                // placeholder
                if text.wrappedValue.isEmpty {
                    Text("Enter Username")
                        .foregroundColor(Color.white.opacity(0.35))
                        .font(.system(size: 16))
                        .padding(.horizontal, 16)
                }

                // actual textfield
                TextField("", text: text)
                    .foregroundColor(.white)
                    .font(.system(size: 16))
                    .padding(.horizontal, 16)
                    .frame(height: 48)
                    .background(Color.clear)
            }
        }
    }
}
