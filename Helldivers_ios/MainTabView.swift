import SwiftUI

extension UIColor {
    static let helldiverYellow = UIColor(red: 255/255, green: 231/255, blue: 16/255, alpha: 1.0)
}

struct MainTabView: View {

    @StateObject private var loadoutsViewModel = LoadoutsViewModel()

    init() {
        let appearance = UITabBarAppearance()
        appearance.configureWithOpaqueBackground()
        appearance.backgroundColor = UIColor.black

        // selected tab
        appearance.stackedLayoutAppearance.selected.iconColor = UIColor.systemYellow
        appearance.stackedLayoutAppearance.selected.titleTextAttributes = [
            .foregroundColor: UIColor.helldiverYellow
        ]

        // unselected tab
        appearance.stackedLayoutAppearance.normal.iconColor = UIColor(white: 0.6, alpha: 1.0)
        appearance.stackedLayoutAppearance.normal.titleTextAttributes = [
            .foregroundColor: UIColor(white: 0.6, alpha: 1.0)
        ]

        UITabBar.appearance().standardAppearance = appearance
        if #available(iOS 15.0, *) {
            UITabBar.appearance().scrollEdgeAppearance = appearance
        }
    }

    var body: some View {
        TabView {
            NavigationStack {
                LoadoutsView()
            }
            .environmentObject(loadoutsViewModel)
            .tabItem {
                Image(systemName: "list.bullet")
                Text("Loadouts")
            }

            NewLoadoutView()
                .environmentObject(loadoutsViewModel)
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
        .tint(.helldiverYellow)
    }
}

