import SwiftUI

extension Color {
    static let helldiverYellow = Color(red: 1.0, green: 231/255.0, blue: 16/255.0)
}

struct WarbondOption: Identifiable, Hashable {
    let id: String
    let label: String
}

private let allWarbonds: [WarbondOption] = [
    .init(id: "BASE",                  label: "Base"),
    .init(id: "STEELED_VETERANS",       label: "Steeled Veterans"),
    .init(id: "HELLDIVERS_MOBILIZE",   label: "Helldivers Mobilize"),
    .init(id: "KILLZONE_CROSSOVER",    label: "Helldivers x Killzone Crossover"),
    .init(id: "VIPER_COMMANDOS",       label: "Viper Commandos"),
    .init(id: "POLAR_PATRIOTS",        label: "Polar Patriots"),
    .init(id: "DEMOCRATIC_DETONATION", label: "Democratic Detonation"),
    .init(id: "FORCE_OF_LAW",          label: "Force of Law"),
    .init(id: "MASTERS_OF_CEREMONY",   label: "Masters of Ceremony"),
    .init(id: "FREEDOMS_FLAME",        label: "Freedom's Flame"),
    .init(id: "ODST",                  label: "ODST"),
    .init(id: "DUST_DEVILS",           label: "Dust Devils"),
    .init(id: "CONTROL_GROUP",         label: "Control Group"),
    .init(id: "BORDERLINE_JUSTICE",    label: "Borderline Justice"),
    .init(id: "SOF",                   label: "Servants of Freedom"),
    .init(id: "TRUTH_ENFORCERS",       label: "Truth Enforcers"),
    .init(id: "URBAN_LEGENDS",         label: "Urban Legends"),
    .init(id: "CUTTING_EDGE",          label: "Cutting Edge"),
    .init(id: "SUPER_STORE",           label: "Super Store"),
    .init(id: "SUPER_CITIZEN_EDITION", label: "Super Citizen Edition"),
    .init(id: "SERVANTS_OF_FREEDOM",   label: "Servants of Freedom"),
    .init(id: "CHEMICAL_AGENTS",       label: "Chemical Agents")
]

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
    @State private var excludedWarbonds: Set<String> = []

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

                VStack(alignment: .leading, spacing: 12) {
                    Text("Warbonds you DON'T own")
                        .foregroundColor(.white)
                        .font(.system(size: 16, weight: .semibold))

                    Text("We'll avoid gear from these warbonds.")
                        .foregroundColor(.white.opacity(0.7))
                        .font(.system(size: 13))

                    ScrollView {
                        LazyVGrid(
                            columns: [
                                GridItem(.flexible()),
                                GridItem(.flexible())
                            ],
                            spacing: 8
                        ) {
                            ForEach(allWarbonds) { wb in
                                let isExcluded = excludedWarbonds.contains(wb.id)

                                Button {
                                    if isExcluded {
                                        excludedWarbonds.remove(wb.id)
                                    } else {
                                        excludedWarbonds.insert(wb.id)
                                    }
                                } label: {
                                    Text(wb.label)
                                        .font(.system(size: 13, weight: .semibold))
                                        .multilineTextAlignment(.center)
                                        .padding(.vertical, 8)
                                        .padding(.horizontal, 10)
                                        .frame(maxWidth: .infinity)
                                        .background(
                                            RoundedRectangle(cornerRadius: 16)
                                                .fill(
                                                    isExcluded
                                                    ? Color.helldiverYellow
                                                    : Color.white.opacity(0.12)
                                                )
                                        )
                                        .foregroundColor(isExcluded ? .black : .white)
                                }
                                .buttonStyle(.plain)
                            }
                        }
                    }
                    .frame(maxHeight: 220)
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

        let warbondArray = Array(excludedWarbonds)

        await viewModel.generateLoadout(
            players: selectedPlayers,
            style: selectedType.apiStyle,
            warbonds: warbondArray
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
