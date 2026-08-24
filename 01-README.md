# London Labour Market Intelligence — Data Analyst Portfolio Project

> **Draft portfolio case study | British English + Traditional Chinese (TW)**

## Executive summary｜執行摘要

This end-to-end analytics project examines labour-market conditions across London boroughs and translates evidence into practical decision support for senior stakeholders.

本專案是一個端到端資料分析（Data Analytics）案例，分析倫敦各 borough 的勞動市場狀況，並將分析結果轉化為管理層可使用的決策支援。

The project combines data preparation, validation, descriptive analysis, priority scoring, robustness testing, intervention mapping and executive dashboard design.

本專案涵蓋資料整理、資料驗證、描述性分析、優先度評分、穩健性／敏感度分析、介入方向 mapping，以及 CEO / executive dashboard 設計。

## Business question｜商業問題

**Where in London should decision-makers focus their attention, and which areas remain priorities when the assumptions behind the analysis are tested?**

**倫敦哪些地區最值得管理層優先關注？當分析假設受到敏感度及穩健性測試後，哪些地區仍然維持優先？**

The aim is not simply to rank boroughs. The aim is to provide an evidence-led framework for deciding **where to investigate further, why an area appears to be a priority, and how confident decision-makers should be in that signal**.

本專案並非單純為 borough 排名，而是建立一套以證據為基礎的框架，協助決策者判斷**應優先調查哪些地區、為何該地區被識別為 priority，以及對該結論應有多大信心**。

## Stakeholder perspective｜利害關係人視角

The primary communication layer is designed for a CEO / senior leadership audience. The dashboard therefore prioritises concise indicators, geographic concentration, robustness and decision implications rather than technical detail.

主要溝通對象設定為 CEO／高階管理層，因此 dashboard 著重於關鍵指標、地理集中程度、分析結果的穩健性，以及對決策的意義，而不是大量技術細節。

## Six CEO metrics｜六項 CEO 關鍵指標

1. **Priority Boroughs｜優先 borough 數量** — number of boroughs classified as High Priority.
2. **Robust Priority Boroughs｜穩健優先 borough 數量** — high-priority boroughs that remain robust under the approved sensitivity framework.
3. **Unemployment Rate｜失業率** — headline labour-market pressure indicator.
4. **Economic Inactivity Rate｜經濟不活躍率** — indicator of participation / exclusion pressure.
5. **Jobs Density｜職位密度** — indicator of local employment opportunity relative to population.
6. **Priority Score / Rank｜優先度分數／排名** — validated composite measure used to support geographic prioritisation.

## Analytical approach｜分析方法

### 1. Data preparation and validation｜資料整理與驗證

The analysis establishes a structured data model, validates key fields and preserves missing observations rather than silently converting them into zero values.

建立結構化資料模型、驗證核心欄位，並保留真正的 missing values，而不是將缺失值錯誤地轉換為 0。

### 2. Descriptive analysis｜描述性分析

The project examines variation between boroughs and identifies geographic patterns across the main labour-market indicators.

分析各 borough 之間的差異，以及主要勞動市場指標的地理分布模式。

### 3. Priority framework｜優先度框架

Multiple indicators are brought together into a validated composite priority framework. The score is treated as a **relative decision-support measure**, not as a causal estimate.

多項指標被整合至經驗證的 composite priority framework。該分數是**相對性的決策支援指標**，並不代表因果關係。

### 4. Robustness and sensitivity｜穩健性與敏感度

Priority results are tested against approved alternative scenarios so that stakeholders can distinguish between stable signals and results that are sensitive to assumptions.

透過既定的 alternative scenarios 測試 priority 結果，讓管理層可以區分穩定的分析訊號與對假設較敏感的結果。

### 5. Intervention mapping｜介入方向 mapping

The analysis translates evidence into suggested areas for further investigation and intervention planning, while avoiding unsupported causal claims.

將分析結果轉化為後續調查及 intervention planning 的方向，同時避免作出沒有證據支持的因果性結論。

## Dashboard product｜Dashboard 產品

The final dashboard concept is designed consistently for **Power BI and Tableau**.

最終 dashboard 概念同時為 **Power BI 及 Tableau** 設計，以保持相同的 business logic。

### Executive Overview｜管理層總覽

- Six CEO KPIs
- Borough priority map
- Priority ranking
- Priority-tier distribution
- Concise executive interpretation

### Borough Detail｜Borough 詳細分析

- Borough selector
- Six key metrics
- Borough versus London benchmark
- Priority and robustness status
- Evidence-informed narrative

### Priority & Robustness｜優先度與穩健性

- Geographic ranking
- Robust priority status
- Sensitivity / scenario view
- Intervention themes

## Technical stack｜技術工具

**Python** — data preparation, exploratory analysis and analytical validation

**SQL** — structured querying and data transformation

**Power BI** — executive dashboard and decision-support visualisation

**Tableau** — parallel dashboard implementation

**Excel** — controlled analytical outputs, reconciliation and handover

## What makes this an analyst project｜資料分析師價值

The value of the project is not simply the use of technical tools. The analyst contribution is the translation from **data → evidence → judgement → decision support**.

本專案的價值並不只是使用 Python、SQL、Power BI 或 Tableau。資料分析師真正的貢獻，是將 **data → evidence → judgement → decision support** 串連起來。

Key analyst responsibilities demonstrated include:

- questioning data quality and assumptions
- validating analytical outputs
- distinguishing correlation / association from causation
- testing robustness rather than relying on a single ranking
- communicating uncertainty
- translating technical results into stakeholder language
- designing decision-oriented dashboards
- maintaining consistent metric definitions across tools

## Limitations｜限制

This project is a decision-support analysis rather than a causal impact evaluation. Priority scores should therefore be interpreted as relative signals for further investigation.

本專案屬於 decision-support analysis，而非 causal impact evaluation。因此 priority score 應被理解為協助後續調查的相對性訊號。

The dashboard should be reconciled against the approved analytical reference before publication, and missing data should remain explicitly identifiable.

正式發布前應將 dashboard 與已核准的 analytical reference 進行 reconciliation，並清楚標示 missing data。

## Portfolio evidence｜作品集證據

The supporting portfolio package contains:

- analytical outputs
- Power BI data model and DAX
- Power BI CEO dashboard build assets
- Tableau CEO dashboard data and calculated fields
- QA and reconciliation materials
- executive recommendations
- interview evidence

## Draft status｜草稿狀態

**This is Draft 1 for review.**

這是 **Draft 1 草稿**，目前重點是確認故事線、定位、語氣及公開作品集結構；數字、圖像、dashboard screenshots、GitHub repository structure and final wording can be refined after review.
