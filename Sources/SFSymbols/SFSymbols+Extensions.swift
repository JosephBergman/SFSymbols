//
//  SFSymbols+Extensions.swift
//  
//
//  Created by JT Bergman on 1/13/20.
//

import Foundation
import SwiftUI



// MARK:- Image

public extension Image {
    
    init(symbol: SFSymbol) {
        self.init(systemName: symbol.rawValue)
    }
}
