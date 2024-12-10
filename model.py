import math
from scipy.stats import norm

# Black-Scholes Call Option Pricing Function
def black_scholes_call(S, K, T, r, sigma):
    # Calculate d1 and d2
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    # Calculate the call option price
    call_price = (S * norm.cdf(d1)) - (K * math.exp(-r * T) * norm.cdf(d2))
    return call_price

# Input parameters from the user
try:
    S = float(input("Enter the current stock price (S): "))
    K = float(input("Enter the strike price (K): "))
    T = float(input("Enter the time to expiration in years (T): "))
    r = float(input("Enter the risk-free interest rate (r) as a decimal (e.g., 0.05 for 5%): "))
    sigma = float(input("Enter the volatility (σ) as a decimal (e.g., 0.20 for 20%): "))

    # Calculate the call option price
    call_option_price = black_scholes_call(S, K, T, r, sigma)

    # Display the result
    print(f"\nThe fair price of the call option is: ${call_option_price:.2f}")
except ValueError:
    print("\nInvalid input. Please enter numerical values.")
