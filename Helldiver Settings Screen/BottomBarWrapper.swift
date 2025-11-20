import SwiftUI
import UIKit

struct BottomBarWrapper: UIViewControllerRepresentable {
    func makeUIViewController(context: Context) -> UIViewController {
        FixedBottomBarViewController()
    }

    func updateUIViewController(_ uiViewController: UIViewController, context: Context) {
        // Nothing to update for now
    }
}
