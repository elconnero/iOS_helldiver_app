import UIKit

class ListIconButton: UIButton {
    
    private let shapeLayer = CAShapeLayer()
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        setup()
    }
    
    required init?(coder: NSCoder) {
        super.init(coder: coder)
        setup()
    }
    
    private func setup() {
        backgroundColor = .clear
        
        // #CCCCCC
        shapeLayer.fillColor = UIColor(
            white: 0.80,
            alpha: 1.0
        ).cgColor
        
        layer.addSublayer(shapeLayer)
    }
    
    override func layoutSubviews() {
        super.layoutSubviews()
        
        // Icon container inside 25x25 button
        let iconLeft: CGFloat = 1.7
        let iconTop: CGFloat = 8.5
        let iconWidth: CGFloat = 21.6
        let iconHeight: CGFloat = 12.0
        
        // 3 rows inside 12pt height: 2 + 3 + 2 + 3 + 2 = 12
        let lineHeight: CGFloat = 2.0
        let spacing: CGFloat = 3.0
        
        // bullets + lines
        let bulletSize: CGFloat = 2.0          // small squares
        let bulletX = iconLeft
        let lineX = bulletX + bulletSize + 2.0 // small gap after bullet
        let lineWidth = iconLeft + iconWidth - lineX
        
        let path = UIBezierPath()
        
        for row in 0..<3 {
            let y = iconTop + CGFloat(row) * (lineHeight + spacing)
            
            // Bullet square
            let bulletRect = CGRect(
                x: bulletX,
                y: y,
                width: bulletSize,
                height: bulletSize
            )
            path.append(UIBezierPath(rect: bulletRect))
            
            // Line bar
            let lineRect = CGRect(
                x: lineX,
                y: y,
                width: lineWidth,
                height: lineHeight
            )
            path.append(UIBezierPath(roundedRect: lineRect, cornerRadius: 1))
        }
        
        shapeLayer.path = path.cgPath
        
        // angle: 0, opacity: 1
        self.transform = .identity
        self.alpha = 1.0
    }
}
