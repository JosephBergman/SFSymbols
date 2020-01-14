import XCTest
import SwiftUI
@testable import SFSymbols

final class SFSymbolsTests: XCTestCase {
    
    // Assert there are > 1,500 symbols
    func testAllCases() {
        XCTAssertTrue(SFSymbol.allCases.count >= 1_500)
    }
    
    // Assert can create an image
    func testImage() {
        XCTAssertNotNil(Image(symbol: SFSymbol.houseFill))
    }
    
    static var allTests = [
        ("testAllCases", testAllCases),
        ("testImage", testImage),
    ]
}
