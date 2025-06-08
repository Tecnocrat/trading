// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CryptoTradingApp {
    struct Position {
        uint256 leverage;
        uint256 amount;
    }

    mapping(address => Position) public tradePositions;

    event PositionOpened(address indexed trader, uint256 leverage, uint256 amount);

    function openPosition(uint256 leverage, uint256 amount) external {
        require(leverage >= 1, "Invalid leverage");
        require(amount > 0, "Amount must be greater than zero");

        tradePositions[msg.sender] = Position(leverage, amount);

        emit PositionOpened(msg.sender, leverage, amount);
    }

    function getPosition(address trader) external view returns (uint256 leverage, uint256 amount) {
        Position memory position = tradePositions[trader];
        return (position.leverage, position.amount);
    }
}
