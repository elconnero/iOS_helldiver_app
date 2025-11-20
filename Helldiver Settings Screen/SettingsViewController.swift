import UIKit

class FixedBottomBarViewController: UIViewController {
    
    private let scrollView = UIScrollView()
    private let contentView = UIView()
    private let bottomBar = UIView()
    private let menuButton = ListIconButton()
    private let loadoutsLabel = UILabel()
    private let ellipseView = UIView()
    private let crossIcon = UIView()
    private let newLoadoutLabel = UILabel()
    private let settingsIcon = UIImageView()
    private let settingsLabel = UILabel()
    private let bigSettingsLabel = UILabel()
    private let settingsRectangle1 = UIView()
    private let settingsRectangle2 = UIView()
    private let settingsRectangle3 = UIView()
    private let settingsRectangle4 = UIView()
    private let username1Label = UILabel()
    private let username2Label = UILabel()
    private let username3Label = UILabel()
    private let username4Label = UILabel()
    private let username1TextField = UITextField()
    private let username2TextField = UITextField()
    private let username3TextField = UITextField()
    private let username4TextField = UITextField()
    private let settingSaveButton = UIButton(type: .system)
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        view.backgroundColor = .black
        setupScrollView()
        setupBottomBar()
        setupMenuButton()
        setupLoadoutsLabel()
        setupEllipse()
        setupCrossIcon()
        setupNewLoadoutLabel()
        setupSettingsIcon()
        setupSettingsLabel()
        setupBigSettingsLabel()
        
        setupUsername1Label()
        setupSettingsRectangle1()
        setupUsername2Label()
        setupSettingsRectangle2()
        setupUsername3Label()
        setupSettingsRectangle3()
        setupUsername4Label()
        setupSettingsRectangle4()
        setupSaveButton()
    }
    
    private func setupScrollView() {
        scrollView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(scrollView)
        
        contentView.translatesAutoresizingMaskIntoConstraints = false
        scrollView.addSubview(contentView)
        contentView.backgroundColor = .black
        
        NSLayoutConstraint.activate([
            scrollView.topAnchor.constraint(equalTo: view.topAnchor),
            scrollView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            scrollView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            scrollView.bottomAnchor.constraint(equalTo: view.bottomAnchor),
            
            contentView.topAnchor.constraint(equalTo: scrollView.contentLayoutGuide.topAnchor),
            contentView.leadingAnchor.constraint(equalTo: scrollView.contentLayoutGuide.leadingAnchor),
            contentView.trailingAnchor.constraint(equalTo: scrollView.contentLayoutGuide.trailingAnchor),
            contentView.bottomAnchor.constraint(equalTo: scrollView.contentLayoutGuide.bottomAnchor),
            
            contentView.widthAnchor.constraint(equalTo: scrollView.frameLayoutGuide.widthAnchor),
            contentView.heightAnchor.constraint(equalToConstant: 1500)
        ])
    }
    
    private func setupBottomBar() {
        bottomBar.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(bottomBar)
        
        bottomBar.backgroundColor = UIColor(
            red: 26/255,
            green: 26/255,
            blue: 26/255,
            alpha: 1.0
        ) // #1A1A1A
        
        NSLayoutConstraint.activate([
            bottomBar.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            bottomBar.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            bottomBar.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            bottomBar.heightAnchor.constraint(equalToConstant: 83)
        ])
    }
    
    private func setupMenuButton() {
        menuButton.translatesAutoresizingMaskIntoConstraints = false
        bottomBar.addSubview(menuButton)
        
        menuButton.alpha = 1.0
        menuButton.transform = .identity
        
        NSLayoutConstraint.activate([
            menuButton.widthAnchor.constraint(equalToConstant: 25),
            menuButton.heightAnchor.constraint(equalToConstant: 25),
            menuButton.leadingAnchor.constraint(equalTo: bottomBar.leadingAnchor, constant: 78),
            menuButton.topAnchor.constraint(equalTo: bottomBar.topAnchor, constant: 4)
        ])
        
        menuButton.addTarget(self, action: #selector(menuTapped), for: .touchUpInside)
    }
    
    @objc private func menuTapped() {
        print("List icon button tapped")
    }
    
    private func setupLoadoutsLabel() {
        loadoutsLabel.translatesAutoresizingMaskIntoConstraints = false
        bottomBar.addSubview(loadoutsLabel)

        loadoutsLabel.text = "Loadouts"
        loadoutsLabel.textColor = UIColor(white: 0.95, alpha: 1.0)
        loadoutsLabel.font = UIFont.systemFont(ofSize: 10, weight: .medium)
        loadoutsLabel.textAlignment = .center

        NSLayoutConstraint.activate([
            loadoutsLabel.topAnchor.constraint(equalTo: menuButton.bottomAnchor, constant: 4),
            loadoutsLabel.centerXAnchor.constraint(equalTo: menuButton.centerXAnchor)
        ])
    }
    
    private func setupEllipse() {
        view.addSubview(ellipseView)
        
        ellipseView.backgroundColor = UIColor(
            red: 63/255,
            green: 63/255,
            blue: 63/255,
            alpha: 1.0
        ) // #3F3F3F
        
        ellipseView.layer.cornerRadius = 22   // 44 / 2
        ellipseView.clipsToBounds = true
        ellipseView.alpha = 1.0
    }
    
    override func viewDidLayoutSubviews() {
        super.viewDidLayoutSubviews()
        
        let barTop = bottomBar.frame.minY
        let ellipseTop = barTop - 17
        let ellipseX = (view.bounds.width - 44) / 2
        
        ellipseView.frame = CGRect(
            x: ellipseX,
            y: ellipseTop,
            width: 44,
            height: 44
        )
        
        let crossSize: CGFloat = 16
        let crossX = ellipseView.frame.midX - crossSize/2
        let crossY = ellipseView.frame.midY - crossSize/2
        
        crossIcon.frame = CGRect(
            x: crossX,
            y: crossY,
            width: crossSize,
            height: crossSize
        )

        let newLabelWidth: CGFloat = 90
        let newLabelHeight: CGFloat = 12
        let newLabelY = barTop + 33
        let newLabelX = ellipseView.frame.midX - newLabelWidth / 2

        newLoadoutLabel.frame = CGRect(
            x: newLabelX,
            y: newLabelY,
            width: newLabelWidth,
            height: newLabelHeight
        )
        
        let iconWidth: CGFloat = 25
        let iconHeight: CGFloat = 25

        let ellipseRight = ellipseView.frame.maxX
        let rightEdge = view.bounds.width

        let midpoint = ellipseRight + (rightEdge - ellipseRight) / 2
        let settingsX = midpoint - (iconWidth / 2)

        let settingsY = barTop + 4

        settingsIcon.frame = CGRect(
            x: settingsX,
            y: settingsY,
            width: iconWidth,
            height: iconHeight
        )
        
        let labelWidth: CGFloat = 41
        let settingsLabelHeight: CGFloat = 12

        let labelX = settingsIcon.frame.midX - (labelWidth / 2)
        let labelY = settingsIcon.frame.maxY + 4

        settingsLabel.frame = CGRect(
            x: labelX,
            y: labelY,
            width: labelWidth,
            height: settingsLabelHeight
        )
        
        let bigWidth: CGFloat = 130
        let bigHeight: CGFloat = 42

        let bigX = (view.bounds.width - bigWidth) / 2
        let bigY: CGFloat = 60

        bigSettingsLabel.frame = CGRect(
            x: bigX,
            y: bigY,
            width: bigWidth,
            height: bigHeight
        )
            
        let horizontalMargin: CGFloat = 24
        let rectHeight: CGFloat = 35
        let rect1Top: CGFloat = 234
        let rect2Top: CGFloat = 316
        let rect3Top: CGFloat = 398
        let rect4Top: CGFloat = 480
        
        username1Label.frame = CGRect(
            x: 24,
            y: 207,
            width: 89,
            height: 19
        )
            
        settingsRectangle1.frame = CGRect(
            x: horizontalMargin,
            y: rect1Top,
            width: view.bounds.width - horizontalMargin * 2,
            height: rectHeight
        )
            
        username1TextField.frame = CGRect(
            x: 0,
            y: 0,
            width: settingsRectangle1.bounds.width,
            height: settingsRectangle1.bounds.height
        )
        
        username2Label.frame = CGRect(
            x: 24,
            y: 289,
            width: 89,
            height: 19
        )
        
        settingsRectangle2.frame = CGRect(
            x: horizontalMargin,
            y: rect2Top,
            width: view.bounds.width - horizontalMargin * 2,
            height: rectHeight
        )
            
        username2TextField.frame = CGRect(
            x: 0,
            y: 0,
            width: settingsRectangle2.bounds.width,
            height: settingsRectangle2.bounds.height
        )
        
        username3Label.frame = CGRect(
            x: 24,
            y: 371,
            width: 89,
            height: 19
        )
        
        settingsRectangle3.frame = CGRect(
            x: horizontalMargin,
            y: rect3Top,
            width: view.bounds.width - horizontalMargin * 2,
            height: rectHeight
        )
            
        username3TextField.frame = CGRect(
            x: 0,
            y: 0,
            width: settingsRectangle3.bounds.width,
            height: settingsRectangle3.bounds.height
        )
        
        username4Label.frame = CGRect(
            x: 24,
            y: 453,
            width: 89,
            height: 19
        )
        
        settingsRectangle4.frame = CGRect(
            x: horizontalMargin,
            y: rect4Top,
            width: view.bounds.width - horizontalMargin * 2,
            height: rectHeight
        )
            
        username4TextField.frame = CGRect(
            x: 0,
            y: 0,
            width: settingsRectangle4.bounds.width,
            height: settingsRectangle4.bounds.height
        )
        
        let saveWidth: CGFloat = 90
        let saveHeight: CGFloat = 47
        let saveY: CGFloat = 551
        let saveX = (view.bounds.width - saveWidth) / 2
        settingSaveButton.frame = CGRect(
            x: saveX,
            y: saveY,
            width: saveWidth,
            height: saveHeight
        )
    }


    
    private func setupCrossIcon() {
        crossIcon.backgroundColor = .clear
        view.addSubview(crossIcon)
        
        let horizontal = UIView()
        horizontal.backgroundColor = UIColor(white: 0.85, alpha: 1)
        horizontal.frame = CGRect(x: 0, y: 7, width: 16, height: 2)
        crossIcon.addSubview(horizontal)
        
        let vertical = UIView()
        vertical.backgroundColor = UIColor(white: 0.85, alpha: 1)
        vertical.frame = CGRect(x: 7, y: 0, width: 2, height: 16)
        crossIcon.addSubview(vertical)
    }
    
    private func setupNewLoadoutLabel() {
        newLoadoutLabel.text = "New Loadout"
        newLoadoutLabel.textColor = UIColor(white: 0.95, alpha: 1.0) // #F2F2F2
        newLoadoutLabel.font = UIFont.systemFont(ofSize: 10, weight: .medium)
        newLoadoutLabel.textAlignment = .center
        newLoadoutLabel.alpha = 1.0
        newLoadoutLabel.adjustsFontSizeToFitWidth = true
        newLoadoutLabel.minimumScaleFactor = 0.7
        newLoadoutLabel.lineBreakMode = .byClipping

        view.addSubview(newLoadoutLabel)
    }
    private func setupSettingsIcon() {
        settingsIcon.image = UIImage(systemName: "gearshape.fill")
        settingsIcon.tintColor = UIColor(
            red: 255/255,
            green: 231/255,
            blue: 16/255,
            alpha: 1.0
        )
        settingsIcon.contentMode = .scaleAspectFit
        settingsIcon.alpha = 1.0
        view.addSubview(settingsIcon)
    }
    
    private func setupSettingsLabel() {
        settingsLabel.text = "Settings"
        settingsLabel.textColor = UIColor(
            red: 255/255,
            green: 231/255,
            blue: 16/255,
            alpha: 1.0
        )
        settingsLabel.font = UIFont.systemFont(ofSize: 10, weight: .medium)
        settingsLabel.textAlignment = .center
        settingsLabel.alpha = 1.0
        settingsLabel.adjustsFontSizeToFitWidth = true
        settingsLabel.minimumScaleFactor = 0.5
        settingsLabel.lineBreakMode = .byClipping
        view.addSubview(settingsLabel)
    }

    private func setupBigSettingsLabel() {
        bigSettingsLabel.text = "Settings"
        bigSettingsLabel.textColor = UIColor(white: 0.95, alpha: 1.0) // #F2F2F2
        if let font = UIFont(name: "ChakraPetch-Bold", size: 32) {
            bigSettingsLabel.font = font
        } else {
            bigSettingsLabel.font = UIFont.systemFont(ofSize: 32, weight: .bold)
        }
        bigSettingsLabel.textAlignment = .center
        bigSettingsLabel.alpha = 1.0
        contentView.addSubview(bigSettingsLabel)
    }
    
    private func setupUsername1Label() {
        username1Label.text = "Username 1"
        username1Label.textColor = UIColor(white: 0.95, alpha: 1.0) // #F2F2F2
        username1Label.font = UIFont.systemFont(ofSize: 16, weight: .regular)
        username1Label.textAlignment = .left
        username1Label.alpha = 1.0
        contentView.addSubview(username1Label)
    }
    
    private func setupSettingsRectangle1() {
        settingsRectangle1.backgroundColor = UIColor(
            red: 0x26/255.0,
            green: 0x26/255.0,
            blue: 0x26/255.0,
            alpha: 1.0
        ) // #262626
        settingsRectangle1.layer.cornerRadius = 8
        settingsRectangle1.clipsToBounds = true
        contentView.addSubview(settingsRectangle1)
        username1TextField.backgroundColor = .clear
        username1TextField.textColor = .white
        username1TextField.font = UIFont.systemFont(ofSize: 16, weight: .regular)
        username1TextField.attributedPlaceholder = NSAttributedString(
            string: "Enter Username",
            attributes: [
                .foregroundColor: UIColor(
                    red: 0xB3/255.0,
                    green: 0xB3/255.0,
                    blue: 0xB3/255.0,
                    alpha: 1.0
                )
            ]
        )
        
        let padding = UIView(frame: CGRect(x: 0, y: 0, width: 12, height: 0))
        username1TextField.leftView = padding
        username1TextField.leftViewMode = .always
        settingsRectangle1.addSubview(username1TextField)
    }

    private func setupUsername2Label() {
        username2Label.text = "Username 2"
        username2Label.textColor = UIColor(white: 0.95, alpha: 1.0) // #F2F2F2
        username2Label.font = UIFont.systemFont(ofSize: 16, weight: .regular)
        username2Label.textAlignment = .left
        username2Label.alpha = 1.0
        contentView.addSubview(username2Label)
    }
    
    private func setupSettingsRectangle2() {
        settingsRectangle2.backgroundColor = UIColor(
            red: 0x26/255.0,
            green: 0x26/255.0,
            blue: 0x26/255.0,
            alpha: 1.0
        ) // #262626
        settingsRectangle2.layer.cornerRadius = 8
        settingsRectangle2.clipsToBounds = true
        
        contentView.addSubview(settingsRectangle2)

        username2TextField.backgroundColor = .clear
        username2TextField.textColor = .white
        username2TextField.font = UIFont.systemFont(ofSize: 16, weight: .regular)

        username2TextField.attributedPlaceholder = NSAttributedString(
            string: "Enter Username",
            attributes: [
                .foregroundColor: UIColor(
                    red: 0xB3/255.0,
                    green: 0xB3/255.0,
                    blue: 0xB3/255.0,
                    alpha: 1.0
                )
            ]
        )
        
        let padding = UIView(frame: CGRect(x: 0, y: 0, width: 12, height: 0))
        username2TextField.leftView = padding
        username2TextField.leftViewMode = .always
        
        settingsRectangle2.addSubview(username2TextField)
    }
    
    private func setupUsername3Label() {
        username3Label.text = "Username 3"
        username3Label.textColor = UIColor(white: 0.95, alpha: 1.0) // #F2F2F2
        username3Label.font = UIFont.systemFont(ofSize: 16, weight: .regular)
        username3Label.textAlignment = .left
        username3Label.alpha = 1.0
        
        contentView.addSubview(username3Label)
    }
    
    private func setupSettingsRectangle3() {
        settingsRectangle3.backgroundColor = UIColor(
            red: 0x26/255.0,
            green: 0x26/255.0,
            blue: 0x26/255.0,
            alpha: 1.0
        ) // #262626
        settingsRectangle3.layer.cornerRadius = 8
        settingsRectangle3.clipsToBounds = true
        
        contentView.addSubview(settingsRectangle3)
        
        username3TextField.backgroundColor = .clear
        username3TextField.textColor = .white
        username3TextField.font = UIFont.systemFont(ofSize: 16, weight: .regular)
        
        username3TextField.attributedPlaceholder = NSAttributedString(
            string: "Enter Username",
            attributes: [
                .foregroundColor: UIColor(
                    red: 0xB3/255.0,
                    green: 0xB3/255.0,
                    blue: 0xB3/255.0,
                    alpha: 1.0
                )
            ]
        )
        
        let padding = UIView(frame: CGRect(x: 0, y: 0, width: 12, height: 0))
        username3TextField.leftView = padding
        username3TextField.leftViewMode = .always
        
        settingsRectangle3.addSubview(username3TextField)
    }
    
    private func setupUsername4Label() {
        username4Label.text = "Username 4"
        username4Label.textColor = UIColor(white: 0.95, alpha: 1.0) // #F2F2F2
        username4Label.font = UIFont.systemFont(ofSize: 16, weight: .regular)
        username4Label.textAlignment = .left
        username4Label.alpha = 1.0
        
        contentView.addSubview(username4Label)
    }
    
    private func setupSettingsRectangle4() {
        settingsRectangle4.backgroundColor = UIColor(
            red: 0x26/255.0,
            green: 0x26/255.0,
            blue: 0x26/255.0,
            alpha: 1.0
        ) // #262626
        settingsRectangle4.layer.cornerRadius = 8
        settingsRectangle4.clipsToBounds = true
        
        contentView.addSubview(settingsRectangle4)
        
        username4TextField.backgroundColor = .clear
        username4TextField.textColor = .white
        username4TextField.font = UIFont.systemFont(ofSize: 16, weight: .regular)
        
        // #B3B3B3
        username4TextField.attributedPlaceholder = NSAttributedString(
            string: "Enter Username",
            attributes: [
                .foregroundColor: UIColor(
                    red: 0xB3/255.0,
                    green: 0xB3/255.0,
                    blue: 0xB3/255.0,
                    alpha: 1.0
                )
            ]
        )
        
        let padding = UIView(frame: CGRect(x: 0, y: 0, width: 12, height: 0))
        username4TextField.leftView = padding
        username4TextField.leftViewMode = .always
        
        settingsRectangle4.addSubview(username4TextField)
    }
    
    private func setupSaveButton() {
        settingSaveButton.setTitle("Save", for: .normal)
        settingSaveButton.setTitleColor(.black, for: .normal)
        settingSaveButton.titleLabel?.font = UIFont.systemFont(ofSize: 16, weight: .semibold)

        // #FFE710
        settingSaveButton.backgroundColor = UIColor(red: 1.0, green: 0.905, blue: 0.063, alpha: 1.0)

        settingSaveButton.layer.cornerRadius = 8
        settingSaveButton.clipsToBounds = true

        contentView.addSubview(settingSaveButton)
    }
}
