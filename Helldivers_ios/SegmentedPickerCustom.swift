import SwiftUI

struct SegmentedPicker: View {
    @State var selectedValue: PickerExampleValue
    @Namespace var pickerAnimation
    @Environment(\.accessibilityReduceMotion) private var reduceMotion
    
    var body: some View {
        HStack {
            ForEach(PickerExampleValue.allCases) { value in
                let isSelected = value == selectedValue
                
                Button(action: {
                    withAnimation(.spring(duration: 0.25)) {
                        selectedValue = value
                    }
                }) {
                    Text(value.rawValue.capitalized)
                        .padding(.horizontal, 12)
                        .padding(.vertical, 6)
                        .font(.subheadline.bold())
                        .foregroundStyle(.white)
                        .background {
                            if isSelected {
                                RoundedRectangle(cornerRadius: 50)
                                    .fill(.tertiary)
                                    .matchedGeometryEffect(id: "background", in: pickerAnimation)
                            }
                        }
                }
                .buttonStyle(.plain)
            }
        }
        .tint(.purple)
        .padding(4)
        .background(
            RoundedRectangle(cornerRadius: 50)
                .fill(.ultraThinMaterial)
        )
    }
}

enum PickerExampleValue: String, Codable, CaseIterable, Identifiable {
    case easy
    case medium
    case hard
    
    var id: String { rawValue }
}

#Preview {
    ZStack {
        LinearGradient(colors: [.black, .indigo], startPoint: .topLeading, endPoint: .bottom)
            .ignoresSafeArea()
     
        VStack {
            Spacer()
            
            SegmentedPicker(
                selectedValue: .easy
            )
        }
    }
}
