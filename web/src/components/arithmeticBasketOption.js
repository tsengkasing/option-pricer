import React, { useState } from 'react';
import InputLabel from '@material-ui/core/InputLabel';
import TextField from '@material-ui/core/TextField';
import Select from '@material-ui/core/Select';
import Button from '@material-ui/core/Button';
import OutlinedInput from '@material-ui/core/OutlinedInput';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import Checkbox from '@material-ui/core/Checkbox';
import CircularProgress from '@material-ui/core/CircularProgress';
import { calcArithmeticBasketOption } from '../util/api';

function ArithmeticBasketOption() {
    const [optionType, setOptionType] = useState('call');
    const [S1, setS1] = useState(100);
    const [S2, setS2] = useState(100);
    const [sigma1, setSigma1] = useState(0.3);
    const [sigma2, setSigma2] = useState(0.3);
    const [r, setR] = useState(0.05);
    const [T, setT] = useState(3.0);
    const [K, setK] = useState(100);
    const [correlation, setCorrelation] = useState(0.5);
    const [m, setM] = useState(100);
    const [control, setControl] = useState(true);
    const [seed, setSeed] = useState(10);
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleInput = {
        'optionType': e => setOptionType(e.target.value),
        'S1': e => setS1(e.target.value),
        'S2': e => setS2(e.target.value),
        'sigma1': e => setSigma1(e.target.value),
        'sigma2': e => setSigma2(e.target.value),
        'r': e => setR(e.target.value),
        'T': e => setT(e.target.value),
        'K': e => setK(e.target.value),
        'correlation': e => setCorrelation(e.target.value),
        'm': e => setM(e.target.value),
        'control': e => setControl(e.target.checked),
        'seed': e => setSeed(e.target.value),
    };

    function handleCalculate() {
        setLoading(true);
        calcArithmeticBasketOption(
            optionType, S1, S2, sigma1, sigma2, r, T, K, correlation, m, control ? 1 : 0, seed
        ).then(data => {
            setResult(data);
            setLoading(false);
        }).catch(err => {
            alert(err);
            setLoading(false);
        });
    }

    return (
        <section className="layout">
            <div className="input__field">
                <FormControl variant="outlined">
                    <InputLabel htmlFor="option-type">Option Type</InputLabel>
                    <Select
                        value={optionType}
                        onChange={handleInput['optionType']}
                        input={
                          <OutlinedInput
                            labelWidth={10}
                            name="option-type"
                            id="option-type"
                          />
                        }
                    >
                    <MenuItem value="call">Call Option</MenuItem>
                    <MenuItem value="put">Put Option</MenuItem>
                    </Select>
                </FormControl>
            </div>
            <div className="input__layout">
                <div className="input__field">
                    <TextField
                        label="Spot price 1 - S1(0)"
                        value={S1}
                        onChange={handleInput['S1']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
                <div className="input__field">
                    <TextField
                        label="Spot price 2 - S2(0)"
                        value={S2}
                        onChange={handleInput['S2']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
                <div className="input__field">
                    <TextField
                        label="Volatility 1 - σ1"
                        value={sigma1}
                        onChange={handleInput['sigma1']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
                <div className="input__field">
                    <TextField
                        label="Volatility 2 - σ2"
                        value={sigma2}
                        onChange={handleInput['sigma2']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
                <div className="input__field">
                    <TextField
                        label="Risk-free Interest Rate - r"
                        value={r}
                        onChange={handleInput['r']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
                <div className="input__field">
                    <TextField
                        label="Time to Maturity - T"
                        value={T}
                        onChange={handleInput['T']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
                <div className="input__field">
                    <TextField
                        label="Strike - K"
                        value={K}
                        onChange={handleInput['K']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
                <div className="input__field">
                    <TextField
                        label="Correlation - ρ"
                        value={correlation}
                        onChange={handleInput['correlation']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
                <div className="input__field">
                    <TextField
                        label="Paths in the Monte Carlo simulation - m"
                        value={m}
                        onChange={handleInput['m']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
                <div className="input__field">
                    <label>Use control variate method</label>
                    <Checkbox
                      checked={control}
                      onChange={handleInput['control']}
                      value="control"
                      color="primary"
                    />
                </div>
                <div className="input__field">
                    <TextField
                        label="Seed"
                        value={seed}
                        onChange={handleInput['seed']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
            </div>
            <Button variant="contained" color="primary" onClick={handleCalculate}>Calculate</Button>
            {loading && <div style={{margin: 16}}><CircularProgress /></div>}
            {result !== null && <div className="calculated-result">
                <span>Result: {result.join(' | ')}</span>
            </div>}
        </section>
    );
}

export default ArithmeticBasketOption;
