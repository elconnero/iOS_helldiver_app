//
//  LoadoutsView.swift
//  Helldivers_ios
//

import SwiftUI

struct LoadoutsView: View {
    @EnvironmentObject var viewModel: LoadoutsViewModel

    var body: some View {
        NavigationStack {
            ZStack {
                Color.black.ignoresSafeArea()
                content
            }
            .navigationBarBackButtonHidden(true)
            .task {
                await viewModel.loadInitial()
            }
        }
    }

    @ViewBuilder
    private var content: some View {
        if viewModel.isLoading && viewModel.loadouts.isEmpty {
            ProgressView("Loading loadout...")
                .tint(.white)
        } else {
            ScrollView {
                VStack(alignment: .leading, spacing: 24) {

                    // Title
                    Text("Loadouts")
                        .font(.custom("ChakraPetch-Bold", size: 34))
                        .foregroundColor(.white)
                        .frame(maxWidth: .infinity, alignment: .center)
                        .padding(.top, 24)

                    if let error = viewModel.errorMessage {
                        Text(error)
                            .foregroundColor(.red)
                            .font(.system(size: 14))
                            .multilineTextAlignment(.center)
                            .padding(.horizontal, 8)
                    }

                    ForEach(viewModel.loadouts) { loadout in
                        loadoutCard(loadout)
                    }

                    Spacer(minLength: 24)
                }
                .padding(.horizontal, 16)
                .padding(.bottom, 16)
            }
        }
    }

    @ViewBuilder
    private func loadoutCard(_ loadout: SquadLoadout) -> some View {
        ZStack {
            RoundedRectangle(cornerRadius: 24)
                .fill(Color.white.opacity(0.06))

            VStack(alignment: .leading, spacing: 12) {
                HStack {
                    Text(loadout.name)
                        .font(.system(size: 20, weight: .semibold))
                        .foregroundColor(.white)

                    Spacer()

                    Button {
                        // ✅ Call the method on the environment object
                        viewModel.delete(loadout)
                    } label: {
                        Image(systemName: "xmark")
                            .foregroundColor(.white.opacity(0.7))
                            .font(.system(size: 16, weight: .bold))
                    }
                    .buttonStyle(.plain)
                }

                Text("\(loadout.playerCount) Players | Type: \(loadout.type.rawValue)")
                    .foregroundColor(.white.opacity(0.7))
                    .font(.system(size: 14))

                HStack {
                    NavigationLink {
                        SquadDetailView(squad: loadout)
                    } label: {
                        Text("View")
                            .font(.system(size: 16, weight: .semibold))
                            .foregroundColor(.black)
                            .frame(width: 96, height: 44)
                            .background(Color.helldiverYellow)
                            .cornerRadius(22)
                    }
                    .buttonStyle(.plain)

                    Spacer()

                    HStack(spacing: 8) {
                        ForEach(0..<5, id: \.self) { _ in
                            RoundedRectangle(cornerRadius: 8)
                                .fill(Color.white.opacity(0.10))
                                .frame(width: 32, height: 32)
                        }
                    }
                }
                .padding(.top, 8)
            }
            .padding(16)
        }
        .frame(maxWidth: .infinity)
        .frame(height: 140)
    }
}

