//
//  SquadDetailView.swift
//  Helldivers_ios
//
//  Created by Alvaro Contreras on 11/29/25.
//

import SwiftUI

struct SquadDetailView: View {
    let squad: SquadLoadout

    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()        // whole screen black

            TabView {
                ForEach(squad.players) { player in
                    PlayerLoadoutView(player: player)
                }
            }
            .tabViewStyle(.page(indexDisplayMode: .automatic))
        }
        // make the nav bar match the app (black)
        .toolbarBackground(.black, for: .navigationBar)
        .toolbarBackground(.visible, for: .navigationBar)
        .toolbarColorScheme(.dark, for: .navigationBar)
    }
}
