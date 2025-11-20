//
//  MainTabView.swift
//  Helldivers_ios
//
//  Created by Alvaro Contreras on 11/20/25.
//

import SwiftUI

struct MainTabView: View {
    var body: some View {
        TabView {
            LoadoutsView()
                .tabItem {
                    Image(systemName: "list.bullet")
                    Text("Loadouts")
                }

            NewLoadoutView()
                .tabItem {
                    Image(systemName: "plus.circle")
                    Text("New Loadout")
                }

            SettingsView()
                .tabItem {
                    Image(systemName: "gearshape")
                    Text("Settings")
                }
        }
        .accentColor(.yellow) // will tweak later
        
        .toolbarBackground(Color.black, for: .tabBar)
        .toolbarBackground(.visible, for: .tabBar)
    }
}
