import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import {map, catchError} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class TickerService {

  private tickerUrl = 'assets/stock-list.txt';

  constructor(private http: HttpClient) { }

  getTickers(): Observable<string[]> {
    return this.http.get(this.tickerUrl, { responseType: 'text' })
      .pipe(
        map(response => response.split('\n')),
        catchError(this.handleError)
      );
  }

  private handleError(error: any) {
    console.error('An error occurred', error);
    return throwError(error.message || error);
  }
}
