//
//  RootView.swift
//  Helldivers_ios
//
//  Created by csuftitan on 10/23/25.
//

import SwiftUI

enum AppRoute {
    case splash
    case mainTabs
}

struct RootView: View {
    @State private var route: AppRoute = .splash

    var body: some View {
        Group {
            switch route {

            case .splash:
                SplashScreenView()
                    .onAppear {
                        DispatchQueue.main.asyncAfter(deadline: .now() + 2.0) {
                            withAnimation {
                                route = .mainTabs
                            }
                        }
                    }

            case .mainTabs:
                MainTabView()
            }
        }
    }
}

#Preview {
    RootView()
}
