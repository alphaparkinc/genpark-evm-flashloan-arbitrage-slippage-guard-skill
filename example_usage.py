from client import EvmFlashloanArbitrageSlippageGuardClient

def main():
    client = EvmFlashloanArbitrageSlippageGuardClient()
    res = client.evaluate_flashloan_slippage_risk()
    print('Flashloan Slippage Guard: ' + res['guard_evaluation_id'] + ' (Safe: ' + str(res['slippage_within_safe_bounds']) + ')')
    print('Impact: ' + str(res['calculated_price_impact_pct']) + '% | MEV Risk: ' + res['sandwich_mev_exposure_risk'])
    print('Simulation URL: ' + res['routing_simulation_url'])

if __name__ == '__main__':
    main()
