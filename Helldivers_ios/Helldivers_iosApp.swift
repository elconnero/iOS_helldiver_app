//
//  Helldivers_iosApp.swift
//  Helldivers_ios
//
//  Created by csuftitan on 10/15/25.
//

import SwiftUI

@main
struct Helldivers_iosApp: App {
    @StateObject private var loadoutsViewModel = LoadoutsViewModel()

    var body: some Scene {
        WindowGroup {
            RootView()
                .environmentObject(loadoutsViewModel)
        }
    }
}
