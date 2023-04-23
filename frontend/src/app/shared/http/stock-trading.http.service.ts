import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import { StockList } from '../model/stock-list-dto.model';
import {  StockInfoList } from '../model/stock-info-list-dto.model.';

@Injectable({
  providedIn: 'root'
})
export class StockTradingService {

  fetchStockListUrl = 'fetch-stock-list';
  updateStockListUrl = 'update-stock-list';
  fetchTradedStockInfoListUrl = 'fetch-traded-stock-info-list';
  runMlModelUrl = 'run-ml-model';
  runTradingSystemUrl = 'run-trading-system';

  constructor(
    private http: HttpClient
  ) { }

  fetchStockList(): Observable<StockList> {
    return this.http.get<StockList>(environment.stockTradingBackendUrl + this.fetchStockListUrl);
  }

  updateStockList(stockList: StockList): Observable<StockList> {
    return this.http.put<StockList>(environment.stockTradingBackendUrl + this.updateStockListUrl, stockList);
  }

  fetchTradedStockInfoList(): Observable<StockInfoList> {
    return this.http.get<StockInfoList>(environment.stockTradingBackendUrl + this.fetchTradedStockInfoListUrl);
  }


  runMlModel(): Observable<String> {
    return this.http.post<String>(environment.stockTradingBackendUrl + this.runMlModelUrl, null);
  }

  runTradingSystem(): Observable<String> {
    return this.http.post<String>(environment.stockTradingBackendUrl + this.runTradingSystemUrl, null);
  }

}