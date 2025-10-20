//
//  ContentView.swift
//  Helldivers_ios
//
//  Created by csuftitan on 10/15/25.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        ZStack {
            Color.yellow
                 .ignoresSafeArea()
            Text("Main Page")
                .foregroundColor(Color.white)
                .font(.system(size: 30))
        }
    }
}

struct ContentView_Preview: PreviewProvider{
    static var previews: some View {
        ContentView()
    }
}

#Preview {
    ContentView()
}
