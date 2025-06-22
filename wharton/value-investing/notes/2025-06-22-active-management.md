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

---

# Market Efficiency & Expected Returns

## Market Efficiency Framework
---

### Cue Column | Notes Section
---|---

**Market Efficiency Definition** | **Stock Prices Reflect All Available Information**
- Efficiency concept | • Market efficiency = stock prices reflect all available information
- Trading implications | • If price reflects all info, you cannot beat the market (whatever you know is already priced in)
- Information timing | • When you learn something good/bad about a stock and go to trade, it's too late

**Expected vs. Needed Return** | **Framework for Evaluating Stock Value**
- Apple example | • AAPL trading at $200, need 10% return annually for risk
- Expected price calculation | • Worth buying if expected price = $220 in one year (+10% of $200)
- Statistical expectation | • Probability-weighted average of all possible future prices
- Pricing evaluation | • Overpriced if expected < $220, Underpriced if expected > $220, Correctly priced if expected = $220

**Efficiency Implications** | **Why Market Efficiency Makes Trading Difficult**
- Information processing | • Many individuals and institutions analyzing stocks deeply (especially large caps like AAPL)
- Trading reality | • If you think you have a fresh angle, consider what it would take for that not to be priced in
- Profitable trades | • Finding profitable trades is not impossible, just harder than it seems

---

# Research Pitfalls in Active Management

## Common Pitfalls When Evaluating Trading Strategies
---

### Cue Column | Notes Section
---|---

**Data Mining (P-Hacking)** | **Searching for Predictive Relations in Databases**
- Definition | • Data mining = searching for predictive relation in database
- Example strategy | • Every time stock X goes up, buy stock Y next day; when X goes down, sell Y
- The problem | • Strategy tested on millions of stock pairs, this combination worked best
- Statistical illusion | • Probability of 1 in million seems impressive, but with 20 million tries, beating those odds becomes likely
- P-value deception | • P-value presented as 0.000001, but real probability much higher due to data mining

**Hold-Out Sample Solution** | **Protecting Against Data Mining**
- Method | • Don't provide all data when looking for strategy
- Example implementation | • Present 10 years of data starting 12 years ago, "hold out" last 2 years
- Testing process | • When trader returns with strategy, apply it to hold-out sample to test effectiveness

**Strategy Lifespan Problem** | **Strategies Have Limited Effectiveness Over Time**
- Historical example | • Small-caps outperformed large-caps in 1980s
- Documentation effect | • Strategy disappeared quickly after being documented
- Profitability decay | • Profitability of strategy likely to fade over time

**Transaction Costs Reality** | **Historical Prices Don't Reflect Actual Trading Costs**
- Price uncertainty | • Don't know what actual trading prices would have been
- Small-cap example | • Stock closed $20 Thursday, $21 Friday ≠ guaranteed 5% return
- Trading reality | • Just because others traded at those prices doesn't mean you could have
- Buyer vs. seller driven | • Important to know if price was buyer or seller driven

**Peso Problem** | **Low-Probability Disaster Risk**
- Historical context | • Mexican Peso stable at $.08 for 20 years before sudden devaluation (late 1970s)
- Popular strategy | • Convert dollars to pesos, earn higher interest, convert back
- The risk | • Strategy bets against low-probability disaster (peso devaluation)
- Problem definition | • Trading strategy betting against rare disaster looks more valuable than it really is

---

# Index Fund Analysis

## Reasons for Index Fund Popularity
---

### Cue Column | Notes Section
---|---

**Low Transaction Costs** | **Minimal Trading Activity Reduces Expenses**
- Index fund trading | • Buys stocks when they enter index, sells when they leave
- Cost advantage | • Buying/selling index rather than individual stocks much cheaper

**No Cost for Average Performance** | **Standard Performance at Minimal Expense**
- S&P 500 index funds | • Gives value-weighted market return with practically no annual fees
- Value proposition | • Pay almost nothing, get average performance
- Cost comparison | • Average performance usually expensive, but free with indexing

**Mean Variance Efficiency** | **Optimal Risk-Return Profile**
- Definition | • Mean variance efficient = minimum risk for expected return
- CAPM prediction | • Value-weighted market portfolio is mean-variance efficient
- Diversification benefit | • Well-diversified portfolio reduces risk

**Index Fund Considerations** | **Potential Drawbacks and Market Impact**
- Universal indexing problem | • Not everyone can index (indiscriminate buying challenges market efficiency)
- Apple example | • If fundamental value $200 but indexing drives price to $300-400, creates inefficiency
- Index correlation | • Stocks added to index move more with index than fundamental value
- Opportunity creation | • Creates opportunities for traders who analyze fundamental value

---

# Jensen's Alpha Analysis

## CAPM Application to Fund Performance
---

### Cue Column | Notes Section
---|---

**Jensen's 1968 Study** | **CAPM Applied to Mutual Fund Performance Analysis**
- Alpha definition | • Alpha = constant term in CAPM regression equation
- Performance measurement | • $r_{i,t} - r_{F,t} = \alpha_i + \beta_i(r_{M,t} - r_{F,t}) + \varepsilon_{i,t}$
- Alpha interpretation | • Positive α = outperforming (excess return above risk-adjusted expectation)
 | • Zero α = performance aligns with risk (CAPM expectation)
 | • Negative α = underperforming

**Jensen's Findings** | **Actively Managed Funds vs. Costs**
- Main conclusion | • On average, actively managed funds did not cover fees and trading costs
- Subsequent studies | • Findings typically replicated with some exceptions
- Investment implication | • Investors better off with low-fee index funds than actively-managed funds

**Fund Manager Ability Considerations** | **Two Important Points About Performance**
- Thousands of funds | • Average performance can be negative even if subset is positive
- Carhart 1997 finding | • Top performers show positive alphas over time
- Fund design problem | • Open-end mutual fund structure hinders even good managers' ability to maintain positive alpha

---

## Hedge Funds

### Cue Column | Notes Section
---|---

**Regulatory Structure** | **Private Funds Avoiding 40 Act Regulation**
- Regulation difference | • Private and less regulated than mutual funds
- 40 Act Fund regulation | • Mutual funds regulated by "40 Act Fund" with disclosure requirements and restrictions
- Public vs. private | • 40 Act Funds are public, hedge funds have choice by limiting investors
- Reporting requirement | • Anyone with >$100M must report equity holdings via Form 13F quarterly

**Compensation Structure** | **Complex Fee Arrangements**
- Management fee | • Usually 2% annually
- Incentive fee | • Usually 20% of profits
- Hurdle rate | • Minimum return threshold before incentive fees
- High-water mark | • Must exceed previous peak value before incentive fees resume
- Vs. mutual funds | • Mutual funds have simple expense ratio structure

**Performance Research** | **Analysis Based on Voluntary Disclosures**
- Public vs. private performance | • 40 Act Fund performance is public, hedge fund performance public only if management wants
- Research limitations | • Hedge fund research relies on voluntary disclosures
- Average performance difficulty | • Hard to assess true average hedge fund performance

**Equity Trading Characteristics** | **Cao, Chen, Goetzmann & Liang (2018) Findings**
- Stock preferences | • Concentrate on smaller, lower-priced, growth, and younger stocks
- Recent performance bias | • Hold more stocks that recently performed very well
- Mispricing focus | • Concentrate on stocks with more potential to be mispriced
- Market efficiency impact | • Stocks tend to become more efficient once hedge funds are involved
- Financial crisis caveat | • Hedge funds quickly dumping stocks during crisis created significant inefficiency