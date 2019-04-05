import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';

import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';

import blue from '@material-ui/core/colors/blue';
import pink from '@material-ui/core/colors/pink';
import Paper from '@material-ui/core/Paper';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';

import EuropeanOption from './components/europeanOption';

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
                <h3>{tabsName[tabIndex]}</h3>
                <div className="tab-container"
                    style={{display: `${tabIndex === 0 ? 'block' : 'none'}`}}>
                    <EuropeanOption />
                </div>
                <div className="tab-container"
                    style={{display: `${tabIndex === 1 ? 'block' : 'none'}`}}>

                </div>
                <div className="tab-container"
                    style={{display: `${tabIndex === 2 ? 'block' : 'none'}`}}>
                </div>
            </div>
        </MuiThemeProvider>
    );
}

ReactDOM.render(<App />, document.getElementById('root'));
