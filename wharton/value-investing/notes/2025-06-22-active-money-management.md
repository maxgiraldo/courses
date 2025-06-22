# Active Money Management

## Mutual Fund Design & Performance Issues
---

### Cue Column | Notes Section
---|---

**Mutual Fund Structure** | **Open-End Design Creates Performance Paradox**
- Open-end funds | • Mutual funds designed as "open-end" - new money flows in when investors buy shares
- Fund flows | • Good performance attracts more investor money into the fund
- Performance impact | • Larger fund size makes it harder to maintain same alpha performance
 | • Bigger trades likely result in worse execution prices (fills)

**Alpha Definition** | **CAPM Framework for Performance Measurement**
- Alpha (α) | • Alpha = constant term in CAPM regression equation
- CAPM equation | • **Formula:** $r_{i,t} - r_{F,t} = \alpha_i + \beta_i(r_{M,t} - r_{F,t}) + \varepsilon_{i,t}$
- Performance indicator | • Positive alpha = outperforming (excess return above risk-adjusted expectation)
 | • Negative alpha = underperforming
 | • Zero alpha = performance aligns with risk (CAPM expectation)

**CAPM Components** | **Key Variables in Capital Asset Pricing Model**
- Returns | • $r_i$ = Return on investment (stock, mutual fund, etc.)
- Risk-free rate | • $r_F$ = Risk-free rate (baseline return)
- Market return | • $r_M$ = Return on the market
- Beta | • $\beta_i$ = Investment's beta × expected market return
- Excess returns | • $E[r_i] - r_F$ = Expected excess return of investment
 | • Market Risk Premium = expected market return above risk-free rate

**Performance Paradox** | **Success Becomes Self-Limiting**
- Fund performance cycle | • Fund 1 underperforms, Fund 2 outperforms → investors move to Fund 2
- Size vs. performance | • Fund 2's success attracts more capital → larger size hurts future performance
- Alpha sustainability | • Higher alpha initially, but harder to maintain with increased assets under management

---

## Summary
The open-end structure of mutual funds creates a fundamental tension: successful performance attracts capital inflows, but larger fund size typically diminishes the manager's ability to generate the same level of alpha. CAPM provides the framework for measuring this alpha - the risk-adjusted excess return that indicates true managerial skill versus market performance.

---

# Mathematical Foundation: Understanding the CAPM Equation

## The Main CAPM Equation Explained

$r_{i,t} - r_{F,t} = \alpha_i + \beta_i(r_{M,t} - r_{F,t}) + \varepsilon_{i,t}$

### Breaking Down Each Symbol

**Left Side of the Equation:**
- $r_{i,t}$ = The actual return of investment $i$ during time period $t$
  - Think: "How much money did my investment make this month?"
  - Example: If you invested $100 and now have $105, your return is 5%

- $r_{F,t}$ = The risk-free rate during time period $t$
  - Think: "What could I earn with zero risk?" (like a government bond)
  - Example: If treasury bills pay 2%, that's your risk-free rate

- $r_{i,t} - r_{F,t}$ = **Excess return** of your investment
  - Think: "How much extra return did I get for taking risk?"
  - Example: 5% investment return - 2% risk-free rate = 3% excess return

**Right Side Components:**

- $\alpha_i$ = **Alpha** - the "magic" of the fund manager
  - Think: "How much extra return does this manager create through skill?"
  - Positive alpha = manager adds value beyond what risk alone would predict
  - Zero alpha = manager performs exactly as expected for the risk taken
  - Negative alpha = manager destroys value

- $\beta_i$ = **Beta** - sensitivity to market movements
  - Think: "How much does this investment move when the market moves?"
  - $\beta = 1$: moves exactly with the market
  - $\beta > 1$: more volatile than market (amplifies market moves)
  - $\beta < 1$: less volatile than market (dampened market moves)
  - Example: If market goes up 10% and your stock goes up 15%, beta might be 1.5

- $r_{M,t}$ = Market return during time period $t$
  - Think: "How did the overall stock market perform?"
  - Usually measured by indices like S&P 500
  - Example: If S&P 500 gained 8% this year, that's your market return

- $(r_{M,t} - r_{F,t})$ = **Market risk premium**
  - Think: "How much extra return does the market provide vs. safe investments?"
  - Example: 8% market return - 2% risk-free rate = 6% market risk premium

- $\beta_i(r_{M,t} - r_{F,t})$ = **Expected excess return due to market risk**
  - Think: "Given this investment's riskiness, how much extra return should I expect?"
  - This is what CAPM theory says you *should* earn for taking market risk

- $\varepsilon_{i,t}$ = **Error term** (epsilon)
  - Think: "Random stuff that happened that we can't predict"
  - Market noise, unexpected events, pure randomness

## The Simplified CAPM Formula

$E[r_i] - r_F = \beta_i(E[r_M] - r_F)$

**What this means in plain English:**
"The extra return you should expect from an investment equals its beta times the extra return you expect from the market."

**Symbol Breakdown:**
- $E[r_i]$ = Expected return of investment $i$
  - The "E" stands for "Expected" - what we think will happen on average
- $E[r_M]$ = Expected return of the market
  - What we think the overall market will return on average

## Real-World Example

Let's say you're looking at a tech stock:
- Risk-free rate: 3%
- Expected market return: 10%
- Stock's beta: 1.2 (20% more volatile than market)

**Using CAPM:**
Expected stock return = 3% + 1.2 × (10% - 3%) = 3% + 8.4% = 11.4%

**If the stock actually returns 13%:**
- Expected return: 11.4%
- Actual return: 13%
- Alpha = 13% - 11.4% = 1.6% (positive alpha - good manager!)

**If the stock actually returns 9%:**
- Expected return: 11.4%
- Actual return: 9%
- Alpha = 9% - 11.4% = -2.4% (negative alpha - poor performance)