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

# Parameters for the option
S = 50          # Stock price today ($)
K = 55          # Strike price ($)
T = 1           # Time to expiration (1 year)
r = 0.05        # Risk-free interest rate (5%)
sigma = 0.20    # Volatility (20%)

# Calculate the call option price
call_option_price = black_scholes_call(S, K, T, r, sigma)

# Display the result
print(f"The fair price of the call option is: ${call_option_price:.2f}")
