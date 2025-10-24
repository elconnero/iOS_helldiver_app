//
//  SplashScreen.swift
//  Helldivers_ios
//
//  Created by csuftitan on 10/20/25.
//

import SwiftUI

struct SplashScreenView: View {
    @State private var isActive = false
    @State private var size: CGFloat = 0.8
    @State private var opacity: Double = 0.5

    let mainUserName: String

    var body: some View {
        // Don’t auto-advance when running in Xcode previews
        let isPreview = ProcessInfo.processInfo.environment["XCODE_RUNNING_FOR_PREVIEWS"] == "1"

        if isActive && !isPreview {
            ContentView()
        } else {
            VStack {
                Image(systemName: "questionmark.circle")
                    .font(.system(size: 80))
                    .foregroundColor(.blue)
                Text("Welcome, \(mainUserName)!")
                Text("HD2 Loadout Generator")
            }
            .scaleEffect(size)
            .opacity(opacity)
            .onAppear {
                withAnimation(.easeIn(duration: 1.2)) {
                    size = 0.9
                    opacity = 1.0
                }
                if !isPreview {
                    DispatchQueue.main.asyncAfter(deadline: .now() + 2.0) {
                        withAnimation { isActive = true }
                    }
                }
            }
        }
    }
}

#Preview("Splash – Guest") {
    SplashScreenView(mainUserName: "Guest")
}

