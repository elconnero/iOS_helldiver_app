//
//  MainTabView.swift
//  Helldivers_ios
//
//  Created by Alvaro Contreras on 11/19/25.
//

import SwiftUI

struct MainTabView: View {
    var body: some View {
        TabView {
            NavigationStack {
                LoadoutsView()
            }
            .tabItem {
                Image(systemName: "list.bullet")
                Text("Loadouts")
            }

            NavigationStack {
                NewLoadoutView()
            }
            .tabItem {
                Image(systemName: "plus.circle")
                Text("New Loadout")
            }

            NavigationStack {
                SettingsView()
            }
            .tabItem {
                Image(systemName: "gearshape")
                Text("Settings")
            }
        }
       // .tint( color )         color for tabs, yellow?
    }
}
