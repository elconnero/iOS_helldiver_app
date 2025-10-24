//
//  RootView.swift
//  Helldivers_ios
//
//  Created by csuftitan on 10/23/25.
//

import SwiftUI

private enum Route { case splash, askUsername, mainMenu }

struct RootView: View {
    @AppStorage("mainUserName") private var mainUserName: String = "Helldiver"
    @AppStorage("mainUserCreateName") private var mainUserCreateName: Bool = false
    @State private var route: Route = .splash

    var body: some View {
        Group {
            switch route {
            case .splash:
                SplashScreenView(mainUserName: mainUserName)
                    .onAppear {
                        DispatchQueue.main.asyncAfter(deadline: .now() + 1.0) {
                            route = mainUserCreateName ? .mainMenu : .askUsername
                        }
                    }

            case .askUsername:
                QueryWindowView { primaryUser in
                    let trimmed = primaryUser.trimmingCharacters(in: .whitespacesAndNewlines)
                    mainUserName = trimmed.isEmpty ? "Helldiver" : trimmed
                    mainUserCreateName = true
                    route = .mainMenu
                }

            case .mainMenu:
                ContentView()
            }
        }
    }
}



private struct RootPreviewBootstrap: View {
    init(username: String?, didOnboard: Bool?) {
        let d = UserDefaults.standard
        if let username { d.set(username, forKey: "mainUserName") }
        else { d.removeObject(forKey: "mainUserName") }

        if let didOnboard { d.set(didOnboard, forKey: "mainUserCreateName") }
        else { d.removeObject(forKey: "mainUserCreateName") }
    }
    var body: some View { RootView() }
}

#Preview("First launch → asks name") {
    RootPreviewBootstrap(username: "Helldiver", didOnboard: false)
}

#Preview("Returning user (Bob) → main") {
    RootPreviewBootstrap(username: "Bob", didOnboard: true)
}


