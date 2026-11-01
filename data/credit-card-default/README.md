# Credit card default data

This dataset describes 30,000 credit card holders at a Taiwanese bank in 2005.
Each row contains a customer's characteristics and six months of bill and payment
history.

The file `credit_card_default.csv.gz` contains 25 columns: 23 potential
predictors, an identifier, and the outcome `default`. There are 6,636 defaults
(22.12%) and 23,364 non-defaults (77.88%). Monetary amounts are in New Taiwan
dollars (NTD).

## Variables

| Variable | Meaning |
| --- | --- |
| `id` | Customer record identifier. |
| `default` | October 2005 outcome: 1 = default payment, 0 = no default payment. |
| `limit_bal` | Granted credit limit in NTD, including supplementary family credit. |
| `sex` | Recorded sex: 1 = male, 2 = female. |
| `education` | 1 = graduate school, 2 = university, 3 = high school, 4 = other. |
| `marriage` | 0 = other marital status, 1 = married, 2 = single, 3 = divorced. |
| `age` | Age in completed years. |
| `pay1` through `pay6` | Monthly repayment-status codes; see below. |
| `bill_amt1` through `bill_amt6` | Monthly bill amounts in NTD. |
| `pay_amt1` through `pay_amt6` | Monthly amounts paid in NTD. |

A credit limit is the amount of credit made available to the customer. A bill
amount is the amount on a monthly statement, while the payment amount records
what the customer paid that month. Bills can be negative, and payments can be
zero. Negative bill amounts can represent a credit balance on the account.

## Monthly histories

The history runs backward from September to April 2005. September is one month
before the October default outcome, so the suffix 1 identifies the first monthly
lag. The suffix 6 identifies April, six months before the outcome.

| Month in 2005 | Repayment status | Bill amount | Amount paid |
| --- | --- | --- | --- |
| September | `pay1` | `bill_amt1` | `pay_amt1` |
| August | `pay2` | `bill_amt2` | `pay_amt2` |
| July | `pay3` | `bill_amt3` | `pay_amt3` |
| June | `pay4` | `bill_amt4` | `pay_amt4` |
| May | `pay5` | `bill_amt5` | `pay_amt5` |
| April | `pay6` | `bill_amt6` | `pay_amt6` |

Repayment status uses the following codes:

| Code | Meaning |
| --- | --- |
| -2 | No card spending. |
| -1 | Paid in full. |
| 0 | Use of revolving credit. |
| 1-8 | Payment delay of the stated number of months. |
| 9 | Payment delay of nine or more months. |

Revolving credit means carrying part of the balance forward to the next billing
period. Repayment status is a categorical variable with information about card
use and payment delays. The outcome `default` records payment performance in the
following month. Its definition does not specify an exact number of overdue days.

## Source and license

Teaching adaptation of Yeh, I. (2009), *Default of Credit Card Clients* [Dataset],
[UCI Machine Learning Repository][uci]. Dataset DOI:
[10.24432/C55S3H][dataset-doi]. Licensed under [Creative Commons Attribution
4.0 International (CC BY 4.0)][license].

Associated study: I-Cheng Yeh and Che-hui Lien (2009), "The comparisons of data
mining techniques for the predictive accuracy of probability of default of
credit card clients," *Expert Systems with Applications*, 36(2), 2473-2480.
[Article DOI][paper-doi].

[uci]: https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients
[dataset-doi]: https://doi.org/10.24432/C55S3H
[paper-doi]: https://doi.org/10.1016/j.eswa.2007.12.020
[license]: https://creativecommons.org/licenses/by/4.0/
