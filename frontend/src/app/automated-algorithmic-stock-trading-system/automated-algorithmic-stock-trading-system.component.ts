import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators, FormControl} from '@angular/forms';
import { TickerService } from '../shared/service/ticker.service';
import {COMMA, ENTER} from '@angular/cdk/keycodes';
import {MatChipInputEvent} from '@angular/material/chips';

@Component({
  selector: 'app-automated_algorithmic-stock-trading-system',
  templateUrl: './automated-algorithmic-stock-trading-system.component.html',
  styleUrls: ['./automated-algorithmic-stock-trading-system.component.css']
})
export class AutomatedAlgorithmicStockTradingSystemComponent implements OnInit{

  addUpdateFormGroup: FormGroup;
  selectable = true;
  removable = true;
  addOnBlur = true;
  readonly separatorKeysCodes = [ENTER, COMMA] as const;

  tickers: string[] = [];

  constructor(private _formBuilder: FormBuilder, private tickerService: TickerService) {
    this.addUpdateFormGroup = this._formBuilder.group({
      stockTickers: new FormControl([], Validators.required)
    });
  }

  ngOnInit() {
    this.tickerService.getTickers()
      .subscribe(tickers => {
        this.tickers = tickers;
        this.addUpdateFormGroup.controls.stockTickers.setValue(tickers);
      });
  }

  add(event: MatChipInputEvent): void {
    const value = (event.value || '').trim();

    if (value) {
      this.tickers.push(value);
    }

    // Clear the input value
    event.chipInput!.clear();
  }

  remove(ticker: string): void {
    const index = this.tickers.indexOf(ticker);

    if (index >= 0) {
      this.tickers.splice(index, 1);
    }
  }

  updateStockList(): void {
    console.log(this.addUpdateFormGroup.controls.stockTickers.value);
  }

  runMlModel(): void {
    console.log('Running ML Model');
  }

  runTradingSystem(): void {
    console.log('Running Trading System');
  }
}
