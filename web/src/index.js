import React, { useState } from 'react';
import ReactDOM from 'react-dom';

import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';

import blue from '@material-ui/core/colors/blue';
import pink from '@material-ui/core/colors/pink';

import EuropeanOption from './components/europeanOption';
import ImpliedVolatility from './components/impliedVolatility';
import AmericanOption from './components/americanOption';
import GeometricAsianOption from './components/geometricAsianOption';
import ArithmeticAsianOption from './components/arithmeticAsianOption';
import GeometricBasketOption from './components/geometricBasketOption';
import ArithmeticBasketOption from './components/arithmeticBasketOption';

// App Theme
const theme = createMuiTheme({
    palette: {
        primary: blue,
        secondary: pink,
    },
    typography: {
        useNextVariants: true,
    },
});

const tabsName = [
    'European Option',
    'Implied Volatility',
    'American Option',
    'Geometric Asian Option',
    'Arithmetic Asian Option',
    'Geometric basket Option',
    'Arithmetic basket Option'
];

function App() {
    const [tabIndex, setTabIndex] = useState(0);
    return (
        <MuiThemeProvider theme={theme}>
            <nav className="nav">
                <ul>
                    {tabsName.map((name, index) => (
                        <li className={`${index === tabIndex ? 'active' : ''}`} key={name}
                            onClick={() => setTabIndex(index)}><span>{name}</span>
                        </li>
                    ))}
                </ul>
            </nav>
            <div className="container">
                <h3 className="tab__title">{tabsName[tabIndex]}</h3>
                <div className="tab-container"
                    style={{display: `${tabIndex === 0 ? 'block' : 'none'}`}}>
                    <EuropeanOption />
                </div>
                <div className="tab-container"
                    style={{display: `${tabIndex === 1 ? 'block' : 'none'}`}}>
                    <ImpliedVolatility />
                </div>
                <div className="tab-container"
                    style={{display: `${tabIndex === 2 ? 'block' : 'none'}`}}>
                    <AmericanOption />
                </div>
                <div className="tab-container"
                    style={{display: `${tabIndex === 3 ? 'block' : 'none'}`}}>
                    <GeometricAsianOption />
                </div>
                <div className="tab-container"
                    style={{display: `${tabIndex === 4 ? 'block' : 'none'}`}}>
                    <ArithmeticAsianOption />
                </div>
                <div className="tab-container"
                    style={{display: `${tabIndex === 5 ? 'block' : 'none'}`}}>
                    <GeometricBasketOption />
                </div>
                <div className="tab-container"
                    style={{display: `${tabIndex === 6 ? 'block' : 'none'}`}}>
                    <ArithmeticBasketOption />
                </div>
            </div>
        </MuiThemeProvider>
    );
}

ReactDOM.render(<App />, document.getElementById('root'));
