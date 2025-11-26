//
//  SplashScreen.swift
//  Helldivers_ios
//
//  Created by csuftitan on 10/20/25.
//

import SwiftUI

struct SplashScreenView: View {
    var body: some View {
        ZStack {
            // Background
            Color.black
                .ignoresSafeArea()

            VStack(spacing: 24) {
                Spacer()

                Image("Helldiver Welcome")
                    .resizable()
                    .scaledToFit()
                    .frame(width: 379, height: 379)

                // Title
                Text("WELCOME HELLDIVER")
                    .font(.custom("ChakraPetch-Bold", size: 32))
                    .kerning(2)
                    .foregroundColor(.white)

                Spacer()

                ProgressView()
                    .progressViewStyle(CircularProgressViewStyle(tint: .helldiverYellow))
                    .scaleEffect(1.2)
                    .padding(.bottom, 60)
            }
            .multilineTextAlignment(.center)
            .padding(.horizontal, 32)
        }
    }
}

#Preview {
    SplashScreenView()
}
