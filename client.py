class EvmFlashloanArbitrageSlippageGuardClient:
    def evaluate_flashloan_slippage_risk(self, pool_id='0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640', loan_amount_usd=5000000.0, max_slippage_tolerance_pct=0.5):
        price_impact_pct = 0.28
        is_safe = price_impact_pct <= max_slippage_tolerance_pct
        return {
            'guard_evaluation_id': 'fl_grd_7719',
            'pool_id': pool_id,
            'loan_amount_usd': loan_amount_usd,
            'calculated_price_impact_pct': price_impact_pct,
            'slippage_within_safe_bounds': is_safe,
            'sandwich_mev_exposure_risk': 'LOW',
            'recommended_split_hops_count': 2,
            'routing_simulation_url': 'https://security.crypto.genpark.ai/flashloan/fl_grd_7719.json'
        }
