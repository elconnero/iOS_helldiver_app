//
//  SplashScreen.swift
//  Helldivers_ios
//
//  Created by csuftitan on 10/20/25.
//

import Foundation
import SwiftUI

struct SplashScreenView: View {
    @State private var isActive = false
    @State private var size = 0.8
    @State private var opacity = 0.5
    
    var body: some View {
        if isActive {
            ContentView()
        } else {
            VStack {
                VStack {
                    Image(systemName: "questionmark.circle")
                        .font(.system(size: 80))
                        .foregroundColor(.blue) // Placeholder, make sure to add B01 helmet or something like that.
                    Text("Welcome, Helldiver!") //Figure out how to get someones name where Helldiver is.
                    Text("HD2 Loadout Generator")
                }
                .scaleEffect(size)
                .opacity(opacity)
                .onAppear {
                    withAnimation(.easeIn(duration: 1.2)) {
                        self.size = 0.9
                        self.opacity = 1.0
                    }
                }
            }
            .onAppear {
                DispatchQueue.main.asyncAfter(deadline: .now() + 2.0) {
                    withAnimation {
                        self.isActive = true
                    }
                }
            }
        }
    }
}

struct SplashScreen_Previews: PreviewProvider {
    static var previews: some View {
        SplashScreenView()
    }
}
