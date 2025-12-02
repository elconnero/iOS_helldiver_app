import SwiftUI

extension Color {
    static let helldiverYellow = Color(red: 1.0, green: 231/255.0, blue: 16/255.0)
}

struct NewLoadoutView: View {

    enum LoadoutType: String, CaseIterable {
        case normal = "Normal"
        case recon = "Recon"
        case explosive = "Explosive"

        /// Map to API "style" strings.
        var apiStyle: String {
            switch self {
            case .normal:    return "default"
            case .recon:     return "spec_ops"
            case .explosive: return "explosive"
            }
        }
    }

    @EnvironmentObject var viewModel: LoadoutsViewModel

    @State private var selectedPlayers: Int = 4
    @State private var selectedType: LoadoutType = .normal
    @State private var isSubmitting: Bool = false
    @State private var submitError: String?

    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()

            VStack(alignment: .leading, spacing: 32) {

                // Title
                Text("New Loadout")
                    .font(.custom("ChakraPetch-Bold", size: 34))
                    .foregroundColor(.white)
                    .frame(maxWidth: .infinity, alignment: .center)
                    .padding(.top, 24)

                // Player count
                VStack(alignment: .leading, spacing: 12) {
                    Text("How many players?")
                        .foregroundColor(.white)
                        .font(.system(size: 16, weight: .semibold))

                    HStack(spacing: 12) {
                        ForEach(1...4, id: \.self) { num in
                            Button {
                                selectedPlayers = num
                            } label: {
                                Text("\(num)")
                                    .font(.system(size: 18, weight: .semibold))
                                    .frame(maxWidth: .infinity)
                                    .frame(height: 48)
                                    .background(
                                        RoundedRectangle(cornerRadius: 12)
                                            .fill(num == selectedPlayers
                                                  ? Color.helldiverYellow
                                                  : Color.white.opacity(0.12))
                                    )
                                    .foregroundColor(num == selectedPlayers ? .black : .white)
                            }
                            .buttonStyle(.plain)
                        }
                    }
                }

                // Loadout Type
                VStack(alignment: .leading, spacing: 12) {
                    Text("Loadout Type")
                        .foregroundColor(.white)
                        .font(.system(size: 16, weight: .semibold))

                    HStack(spacing: 0) {
                        ForEach(LoadoutType.allCases, id: \.self) { type in
                            Button {
                                selectedType = type
                            } label: {
                                Text(type.rawValue)
                                    .font(.system(size: 16, weight: .semibold))
                                    .frame(maxWidth: .infinity)
                                    .frame(height: 44)
                                    .background(
                                        Group {
                                            if selectedType == type {
                                                Color.helldiverYellow
                                            } else {
                                                Color.clear
                                            }
                                        }
                                    )
                                    .foregroundColor(
                                        selectedType == type ? .black : .white
                                    )
                            }
                            .buttonStyle(.plain)
                        }
                    }
                    .padding(.horizontal, 4)
                    .background(Color.white.opacity(0.12))
                    .clipShape(Capsule())
                }

                if let submitError {
                    Text(submitError)
                        .foregroundColor(.red)
                        .font(.system(size: 14))
                }

                Spacer()

                // Create Loadout
                Button {
                    Task {
                        await submit()
                    }
                } label: {
                    HStack(spacing: 8) {
                        if isSubmitting {
                            ProgressView()
                                .tint(.black)
                        } else {
                            Image(systemName: "star.fill")
                                .font(.system(size: 18, weight: .bold))
                        }
                        Text(isSubmitting ? "Creating..." : "Create Loadout")
                            .font(.system(size: 18, weight: .semibold))
                    }
                    .foregroundColor(.black)
                    .padding(.vertical, 14)
                    .frame(maxWidth: 340)
                    .background(Color.helldiverYellow)
                    .cornerRadius(24)
                }
                .disabled(isSubmitting)
                .frame(maxWidth: .infinity)
                .padding(.bottom, 40)
            }
            .padding(.horizontal, 24)
        }
    }

    private func submit() async {
        isSubmitting = true
        submitError = nil

        await viewModel.generateLoadout(
            players: selectedPlayers,
            style: selectedType.apiStyle,
            warbonds: []   // you can add a UI to pick warbonds later
        )

        if let error = viewModel.errorMessage {
            submitError = error
        }

        isSubmitting = false
    }
}

#Preview {
    NewLoadoutView()
        .environmentObject(LoadoutsViewModel())
}

