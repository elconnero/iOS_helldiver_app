//
//  QueryWindow.swift
//  Helldivers_ios
//
//  Created by csuftitan on 10/23/25.
//

import Foundation
import SwiftUI


import SwiftUI

struct QueryWindowView: View {
    var onSubmit: (String) -> Void
    @State private var primaryUser: String = ""

    var body: some View {
        VStack {
            Text("Helldiver, what is your name?")
                .font(.largeTitle).bold().padding()
                .multilineTextAlignment(.center)

            TextField("Username: John Helldiver", text: $primaryUser)
                .padding()
                .frame(width: 300, height: 50)
                .background(Color.black.opacity(0.05))
                .cornerRadius(10)
                .submitLabel(.done)
                .onSubmit { onSubmit(primaryUser) }
                .padding()
        }
    }
}

#Preview {
    QueryWindowView { _ in /* preview no-op */ }
}

