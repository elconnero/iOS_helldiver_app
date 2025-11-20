import SwiftUI

struct ContentView: View {
    var body: some View {
        BottomBarWrapper()
            .background(Color.black)   // <-- Entire screen black
            .ignoresSafeArea()
    }
}

#Preview {
    ContentView()
}
