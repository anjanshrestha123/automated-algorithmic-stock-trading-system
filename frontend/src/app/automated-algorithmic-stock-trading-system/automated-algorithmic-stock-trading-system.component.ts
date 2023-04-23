import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, FormControl } from '@angular/forms';
import { COMMA, ENTER } from '@angular/cdk/keycodes';
import { MatChipInputEvent } from '@angular/material/chips';
import { AfterViewInit, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { StockTradingService } from '../shared/http/stock-trading.http.service';
import { StockList } from '../shared/model/stock-list-dto.model';
import { StockInfo } from '../shared/model/stock-info-dto.model';
import { MatStepper } from '@angular/material/stepper';


@Component({
  selector: 'app-automated_algorithmic-stock-trading-system',
  templateUrl: './automated-algorithmic-stock-trading-system.component.html',
  styleUrls: ['./automated-algorithmic-stock-trading-system.component.css']
})
export class AutomatedAlgorithmicStockTradingSystemComponent implements OnInit, AfterViewInit {

  addUpdateFormGroup: FormGroup;
  selectable = true;
  removable = true;
  addOnBlur = true;
  readonly separatorKeysCodes = [ENTER, COMMA] as const;

  tickers: string[] = [];
  isStockListFetching: boolean = false;
  isStockInfoListFetching: boolean = false;
  isMlModelRunning: boolean = false;
  isTradingSystemRunning: boolean = false;

  displayedColumns: string[] =
    [
      'date_time',
      'stock_ticker',
      'current_price',
      'threshold_signal_price',
      'take_profit_signal_price',
      'stop_loss_price',
      'quantity'
    ];
  dataSource: MatTableDataSource<StockInfo> = new MatTableDataSource();
  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(
    private _formBuilder: FormBuilder,
    private stockTradingService: StockTradingService) {

    this.addUpdateFormGroup = this._formBuilder.group({
      stockTickers: new FormControl([], Validators.required)
    });
  }

  ngOnInit() {

    // Starts the spinner
    this.isStockListFetching = true;

    // Populate stock list
    this.stockTradingService.fetchStockList().subscribe(data => {
      if (data) {
        this.updateStock(data);
        this.isStockListFetching = false;
      }
    });

    // Populate traded stock info
    this.populateTradedStockInfoList();
  }

  ngAfterViewInit() {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
  }

  add(event: MatChipInputEvent): void {
    const value = (event.value || '').trim();

    if (value) {
      this.tickers.push(value);
      this.addUpdateFormGroup.controls.stockTickers.setValue(this.tickers);
    }

    // Clear the input value
    event.chipInput!.clear();
  }

  remove(ticker: string): void {
    const index = this.tickers.indexOf(ticker);

    if (index >= 0) {
      this.tickers.splice(index, 1);
      this.addUpdateFormGroup.controls.stockTickers.setValue(this.tickers);
    }
  }

  updateStockList(): void {
    // Starts the spinner
    this.isStockListFetching = true;
    let stockList: StockList = new StockList(this.addUpdateFormGroup.controls.stockTickers.value);

    this.stockTradingService.updateStockList(stockList).subscribe(data => {
      if (data) {
        this.updateStock(data);

        // Stops the spinnner
        this.isStockListFetching = false;
      }
    });
  }

  populateTradedStockInfoList(): void {
    // Starts the spinner
    this.isStockInfoListFetching = true;

    this.stockTradingService.fetchTradedStockInfoList().subscribe(data => {
      if (data) {

        // Assign the data to the data source for the table to render
        this.dataSource = new MatTableDataSource(data.stock_info_list);

        // Assign the paginator *after* dataSource is set
        this.dataSource.paginator = this.paginator;
        this.dataSource.sort = this.sort;

        // Stops the spinnner
        this.isStockInfoListFetching = false;
      }
    });
  }

  runMlModel(stepper: MatStepper): void {
    // Starts the spinner
    this.isMlModelRunning = true;

    this.stockTradingService.runMlModel().subscribe(() => {

      // Stops the spinnner
      this.isMlModelRunning = false;

      // Move to next step
      stepper.next();
    });
  }

  runTradingSystem(): void {

    this.stockTradingService.runTradingSystem().subscribe(() => {
      console.log('Started Trading System')
    });
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  private updateStock(data: StockList): void {
    this.tickers = data.stock_list;
    this.addUpdateFormGroup.controls.stockTickers.setValue(data.stock_list);
  }
}
