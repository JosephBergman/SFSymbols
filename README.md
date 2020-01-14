# SF Symbols
A better way to use Apple's SF Symbols.


## Introduction 
SF Symbols were introduced during [WWDC 2019](https://medium.com/r/?url=https%3A%2F%2Fdeveloper.apple.com%2Fvideos%2Fplay%2Fwwdc2019%2F206%2F) and provide a set of over 1,500 configurable symbols for use in apps. SF Symbols are designed to integrate beautifully with the San Francisco system font, making it even easier for you to design beautiful iOS, macOS, tvOS, and watchOS apps. SF Symbols can be easily customized to be used as tab bar items, navigation bar items, or buttons throughout your app.


## Problem 
The only issue with SF Symbols is you have to type out the symbol name each time you want to use the symbol. This means you have no auto-completion to help you spell out the symbol name, and you may have to look up the symbol name every single time you want to use it (side note: you can view the symbols using the [SF Symbols App](https://medium.com/r/?url=https%3A%2F%2Fdeveloper.apple.com%2Fdesign%2Fdownloads%2FSF-Symbols.dmg)). This may not seem like a big deal, but some of the icon names are quite long, for example:
```
Image(systemName: "person.crop.circle.badge.checkmark.fill")
Image(systemName: "square.fill.and.line.vertical.square.fill")
Image(systemName: "line.horizontal.3.decrease.circle.fill")
Image(systemName: "arrowshape.turn.up.left.circle.fill")
Image(systemName: "dot.radiowaves.left.and.right")
```


## Solution 
Instead of typing the symbols out each time we want to use them, we can define an enumeration where each case identifies a symbol. Then each symbol's name can be retrieved using dot notation. For example, we first define an enumeration like the following:
```swift 
public enum SFSymbol: String, CaseIterable {
  // MARK: Symbols - A
  case a = "a"
  case aCircle = "a.circle"
  case aCircleFill = "a.circle.fill"
  case aSquare = "a.square"
  case aSquareFill = "a.square.fill"

  // ~1,490 other symbols

  // MARK: Symbols - Z
  case zCircle = "z.circle"
  case zCircleFill = "z.circle.fill"
  case zSquare = "z.square"
  case zSquareFill = "z.square.fill"
  case zzz = "zzz"
}
```

Then, we can create extensions that take an SFSymbol to create images, text, tab buttons, etc. The following code allows us to create a SwiftUI Image using the SFSymbol enumeration.
```swift 
// SwiftUI
extension Image {
  init(symbol: SFSymbol) {
    self.init(systemName: symbol.rawValue)
  }
}
// Usage 
Image(symbol: SFSymbol.zzz)
```


## Usage

### Add SFSymbols 
Go to Xcode > File > Swift Packages > Add Package Dependency and paste 
```
https://github.com/JosephBergman/SFSymbols
```

### Generating SFSymbols 
The [SFSymbols.py](https://github.com/JosephBergman/SFSymbols/blob/master/Symbols/SFSymbols.py) file contains code for scraping the symbol names from the internet and generating the [SFSymbols.swift](https://github.com/JosephBergman/SFSymbols/blob/master/Sources/SFSymbols/SFSymbols.swift) file. To run this file, you will need to have python 3, BeautifulSoup 4, and Requests installed. Then just run 
```
python SFSymbols.py
```


## Read More 
Here are two articles about this library. The first is why it was created and the second is how. 
1. [A Better Way to Use SF Symbols](https://medium.com/@josephbergman/a-better-way-to-use-sf-symbols-237fabdf381)
2. [Creating an SFSymbols Library](https://medium.com/@josephbergman/creating-an-sf-symbols-library-2fbec8ba8dd1)
