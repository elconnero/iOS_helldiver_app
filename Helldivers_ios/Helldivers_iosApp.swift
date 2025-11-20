//
//  Helldivers_iosApp.swift
//  Helldivers_ios
//
//  Created by csuftitan on 10/15/25.
//

import SwiftUI

@main
struct Helldivers_iosApp: App {
    
    init() {
            UITabBar.appearance().unselectedItemTintColor = UIColor(white: 0.70, alpha: 1)
        }
    
    var body: some Scene {
        WindowGroup {
            RootView() 
        }
    }
}

