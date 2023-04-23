import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AutomatedAlgorithmicStockTradingSystemComponent } from './automated-algorithmic-stock-trading-system/automated-algorithmic-stock-trading-system.component';

const routes: Routes = [
  { path: 'stock-trading-system', component: AutomatedAlgorithmicStockTradingSystemComponent, pathMatch: 'full' },
  { path: '**', redirectTo: '/stock-trading-system' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes,{useHash: true})],
  exports: [RouterModule]
})
export class AppRoutingModule { }
